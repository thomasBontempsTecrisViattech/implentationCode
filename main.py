import os
import json

from multiprocessing import Process, freeze_support
from variable import FOLDER_RESUME, PATH_JSON_SCHEMA, FOLDER_DOCX, FOLDER_IMAGE, FOLDER_JSON, FOLDER_JSON_SCHEMA
from resumeToJson import resumeToJson
from jsonToDoc import create_template

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
    init_folder([FOLDER_DOCX, FOLDER_IMAGE, FOLDER_JSON, FOLDER_JSON_SCHEMA])     
    
    
    print("\n\nPour que le programme se lance, il faut obligatoirement 1 CV au format pdf dans le dossier : " + FOLDER_RESUME)
    pdf_files = [file for file in os.listdir(FOLDER_RESUME) if file.lower().endswith('.pdf')]
    json_schema_part_files = [json_schema_file for json_schema_file in os.listdir(FOLDER_JSON_SCHEMA) if json_schema_file.lower().endswith('.json')]
    
    if pdf_files:
        for pdf_file in pdf_files:
            print("\n\n#################### Conversion de PDF en JSON #############################")
            print("\nPrise en charge du fichier : ", pdf_file)
            
            for json_schema_part_file in json_schema_part_files:
                with open(FOLDER_JSON_SCHEMA + '/' + json_schema_part_file) as json_file:
                    json_schema = json.load(json_file)
            
                print("\nTraitement du schema : ", json_schema_part_file,"\n")
                resumeToJson(json_filename=json_schema_part_file, json_schema=json_schema, file_input=pdf_file)    
            
            #print("\n\n#################### Conversion de JSON en DOCX #############################\n")
            
            #create_template(pdf_file[:-3] +'json')
    else:
        print("Pas de CV au format pdf dans le dossier : ", FOLDER_RESUME, "\npdf_files = ", pdf_files)
        
    
    
    print("\n\n###########################################################################")
    print("############################### FIN #######################################")
    print("###########################################################################")
    

if __name__ == '__main__':
    freeze_support()
    Process(target=main).start()