import os
import json

from multiprocessing import Process, freeze_support
from variable import FOLDER_RESUME, FOLDER_DOCX, FOLDER_IMAGE, FOLDER_JSON, FOLDER_JSON_SCHEMA, FOLDER_DONE, FOLDER_TXT
from resumeToJson import resumeToJson
from extractFromPdf import extract_content_from_pdf
from jsonToDoc import create_template
from get_json_openai import get_json_from_text

def init_folder(folders):
    for folder in folders:
        try:
            os.makedirs(folder)
        except:
            print(folder + " existe déjà.")

def main():
    print("###########################################################################")
    print("#################### Conversion de CV en DOCX #############################")
    print("###########################################################################")
    print("\n\nVérifier que les variables correspondent à votre environnement")
    
    print("\n\nCréation des dossiers :")
    init_folder([FOLDER_DOCX, FOLDER_IMAGE, FOLDER_JSON, FOLDER_JSON_SCHEMA, FOLDER_DONE, FOLDER_TXT])     
    
    
    print("\n\nPour que le programme se lance, il faut obligatoirement 1 CV au format pdf dans le dossier : " + FOLDER_RESUME)
    pdf_files = [file for file in os.listdir(FOLDER_RESUME) if file.lower().endswith('.pdf')]
    json_schema_part_files = [json_schema_file for json_schema_file in os.listdir(FOLDER_JSON_SCHEMA) if json_schema_file.lower().endswith('.json')]
    
    ("\n\n#################### Conversion de PDF en JSON #############################")
    API_choice = input("\nQuel méthode souhaitez-vous utiliser pour parser le document (1 ou 2) : \n1. Avec un modèle en local\n2. Avec l'API OpenAI\n\nReponse : ") 

    if pdf_files:
        for pdf_file in pdf_files:
            created = False
            print("\n\nPrise en charge du fichier : ", pdf_file)
            
            text_from_pdf = extract_content_from_pdf(FOLDER_RESUME + '/' + pdf_file)
            with open(FOLDER_TXT + '/' + pdf_file[:-4] + '.txt', "w+") as text_file:
                text_file.write(text_from_pdf)
                
            print("\nLe document pdf a bien été transformé en fichier texte\n")
            
            if API_choice == '1':
                for json_schema_part_file in json_schema_part_files:
                    with open(FOLDER_JSON_SCHEMA + '/' + json_schema_part_file) as json_file:
                        json_schema = json.load(json_file)
                
                    print("\nTraitement du schema : ", json_schema_part_file,"\n")
                    resumeToJson(json_filename=json_schema_part_file, json_schema=json_schema, file_input=pdf_file, content=text_from_pdf)    
            else:
                get_json_from_text(filename=pdf_file, json_schema_files=json_schema_part_files)
            
            
            print("\n\n#################### Conversion de JSON en DOCX #############################\n")
            created = create_template(pdf_file[:-4])
            if created:
                os.replace(FOLDER_RESUME + '/' + pdf_file, FOLDER_DONE + '/' + pdf_file)
            
            break
    else:
        print("Pas de CV au format pdf dans le dossier : ", FOLDER_RESUME, "\npdf_files = ", pdf_files)
        
    
    
    print("\n\n###########################################################################")
    print("############################### FIN #######################################")
    print("###########################################################################")
    

if __name__ == '__main__':
    #freeze_support()
    #Process(target=main).start()
    main() # Le multiprocessing empêche la lecture d'input