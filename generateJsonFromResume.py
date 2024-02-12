from HuggingFaceLLM import HuggingFaceLLM

def extract_structured_data(content: str, json_schema):
    llm = HuggingFaceLLM()  # Choose the desired Hugging Face model
    
    template = """
    Context:
    The resume is below and delimited by --START-- and --END--. You will use this resume to extract the information. 
    Your role is to have an recruiter point of vue to permit of respond the best at the json schema.
    
    
    Goal: 
    Your goal is to : {goal}
    
    Criteria:  
    * Recreate paragraphes with only informations wanted
    * You will decompose the resume in distinct part to extract
    * Use paragraph to extract most precise information or context
    * If multiple choice as answer, create a list of answers
    
    Response format: 
    * No accent at all
    * Consistence phrase
    
    
    --START--

    {content}
    
    --END--
    
    """
    
    # Fill in the placeholders in the template
    formatted_template = template.format(goal=json_schema["description"], content=content)#, data_points=data_points)
    
    # Generate text using the formatted template
    results = llm.generate(prompt=formatted_template,
                           json_schema=json_schema,)

    return results