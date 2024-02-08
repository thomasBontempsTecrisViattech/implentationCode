import os
import json

from multiprocessing import Process, freeze_support
from implentationCode.variable import FOLDER_RESUME, PATH_JSON_SCHEMA, FOLDER_JSON
from implentationCode.resumeToJson import resumeToJson
from implentationCode.jsonToDoc import create_template



def main():
    print("###########################################################################")
    print("#################### Conversion de CV en DOCX #############################")
    print("###########################################################################")
    print("\n\nVérifier que les variables correspondent à votre environnement")
    print("Pour que le programme se lance, il faut obligatoirement 1 CV au format pdf dans le dossier : " + FOLDER_RESUME)
    
    pdf_files = [file for file in os.listdir(FOLDER_RESUME) if file.lower().endswith('.pdf')]
    
    if pdf_files:
        for pdf_file in pdf_files:
            print("\n\n#################### Conversion de PDF en JSON #############################")
            print("\nPrise en charge du fichier : ", pdf_file)
            
            json_schema = json.load(PATH_JSON_SCHEMA)
            resumeToJson(json_schema=json_schema, file_input=pdf_file)    
            
            print("\n\n#################### Conversion de JSON en DOCX #############################\n")
            
            create_template(pdf_file[:-3] +'json')
    
    

if __name__ == '__main__':
    freeze_support()
    Process(target=main).start()