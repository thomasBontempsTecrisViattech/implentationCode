import os
import json
import time

from variable import ASSISTANT_ID, FOLDER_TXT, FOLDER_JSON_SCHEMA, FOLDER_JSON, FOLDER_EXAMPLE
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def get_json_from_text(filename, json_schema_files):
    # Ajouter un fichier (CV) à l'assistant
    try:
        # Delete files in the assistant    
        list_files_assistant = client.beta.assistants.files.list(
            assistant_id=ASSISTANT_ID
        )
        print(list_files_assistant)
        
        for file_assistant in list_files_assistant:
            print(file_assistant)
            client.beta.assistants.files.delete(
                assistant_id=ASSISTANT_ID,
                file_id=file_assistant.id,
            )
    except:
        pass
    
    # Load text file in assistant
    file_loaded = client.files.create(
        file=open(FOLDER_TXT + '/' + filename[:-3] + 'txt', "rb"),
        purpose='assistants'
    )
    client.beta.assistants.files.create(
        assistant_id = ASSISTANT_ID,
        file_id=file_loaded.id
    )
    
    # Création d'un thread 
    thread = client.beta.threads.create()
    
    # What we ask to Assistant
    content = "Extract information from the document to obtain a JSON file corresponding to the following JSON schema:\n{json_schema}\n\nAn example output :\n{example}\n\nGive me the json file only"
    
    # Où seront stocké les fichiers
    folder_stock_json = FOLDER_JSON + '/' + filename[:-4] 
    try:
        os.makedirs(folder_stock_json)
    except:
        pass
    
    for json_schema_file in json_schema_files:
        json_example = json.load(open(FOLDER_EXAMPLE) + '/' + json_schema_file.split('_')[1], 'r')
        json_schema = json.load(open(FOLDER_JSON_SCHEMA + '/' + json_schema_file, 'r'))
        content_formatted = content.format(json_schema=json_schema, example=json_example)
        
        # Mise en place du message dans le thread
        client.beta.threads.messages.create(
            thread_id = thread.id, # ID du thread précédent
            role = 'user', # Role correspond 
            content = content_formatted # Message du rôle
        )
    
        # Création de la session
        run = client.beta.threads.runs.create(
            thread_id = thread.id, # Toujours le même thread
            assistant_id = ASSISTANT_ID # ID de l'assistant pour traiter du thread
        )   
        
        while run.status != "completed":
            time.sleep(0.5)
            # Reload la session pour récupérer la réponse
            run = client.beta.threads.runs.retrieve( 
                thread_id = thread.id,
                run_id = run.id
            )

        # Stocker l'information sous forme de liste de message
        messages = client.beta.threads.messages.list( 
            thread_id = thread.id
        )
        
        message = messages.data[0]
        json_data = {}
        try:
            val = message.content[0].text.value
            if val != "":
                val = val[val.find('{'):]
                json_data = json.loads(val)        
            with open(folder_stock_json + '/' + json_schema_file.split('_')[1], 'w') as json_file:
                json.dump(json_data, json_file)
        except:
            pass

    client.beta.threads.delete(
        thread_id=thread.id
    )    
    return True

    
    
    