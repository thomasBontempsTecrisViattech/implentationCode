import time
import json

from implentationCode.exctractFromPdf import extract_content_from_pdf
from implentationCode.generateJsonFromResume import extract_structured_data
from implentationCode.variable import FOLDER_RESUME, FOLDER_JSON



def resumeToJson(json_schema, file_input):
    
    start_time = time.time()  # Record the start time
    content = extract_content_from_pdf(FOLDER_RESUME + '/' + file_input)
    data = extract_structured_data(content, json_schema)
    json_data = json.dumps(data)
    with open(FOLDER_JSON + '/' + file_input[:-3] + 'json','w') as json_file:
        json_file.write(json_data)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print("Temps pour un CV :", elapsed_time)                
        
