import os 
import time
import json
from implentationCode.exctractFromPdf import extract_content_from_pdf
from implentationCode.generateJsonFromResume import extract_structured_data
from tempfile import NamedTemporaryFile



def resumeToJson(json_schema,
                 file_input = "CV Thomas français.pdf",
                 folder_input='implementationCode/Data/resumes', 
                 folder_output='implementationCode/Data/JSON/resumesJSON',):
    
    print("################################### Resume To JSON #####################################")

    if file_input.lower().endswith('.pdf'):
        start_time = time.time()  # Record the start time
        content = extract_content_from_pdf(folder_input + '/' + file_input)
        data = extract_structured_data(content, json_schema)
        json_data = json.dumps(data)
        with open(folder_output + '/' + file_input,'w') as json_file:
            json_file.write(json_data)
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        print("time for a resume :", elapsed_time)                
        
