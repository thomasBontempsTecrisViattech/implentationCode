import time
import json
import os

from generateJsonFromResume import extract_structured_data
from variable import FOLDER_TXT, FOLDER_JSON



def resumeToJson(json_filename, json_schema, file_input, content):
    start_time = time.time()  # Record the start time
    data = extract_structured_data(content, json_schema)
    json_data = json.dumps(data)
    folder_stock_json = FOLDER_JSON + '/' + file_input[:-4] 
    try:
        os.makedirs(folder_stock_json)
    except:
        pass
    with open(folder_stock_json + '/' + json_filename.split('_')[1], 'w') as json_file:
        json_file.write(json_data)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print("Temps pour ", json_filename, " : ", elapsed_time)                
        
