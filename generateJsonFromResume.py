from HuggingFaceLLM import HuggingFaceLLM

def extract_structured_data(content: str, json_schema):
    llm = HuggingFaceLLM()  # Choose the desired Hugging Face model
    
    template = """
    Context:
    The resume is below and delimited by --START-- and --END--. You will use this resume to extract informations. 
    You have to follow the section Goal and Criteria after --END--.
    
    --START--

    {content}
    
    --END--
    
    IMPORTANT THING TO DO BELLOW :
    Goal: 
    Your goal is to provide : {goal}
    
    Criteria:  
    * Make sure to include all the properties mentioned
    * Recreate paragraphes with only informations wanted
    * You will redecompose the resume in distinct part to extract
    * Use paragraph to extract most precise information or context
    * Process multiple choice as answer, create a list of answers
    * If multiple response, try to find one more
    
    Response format: 
    * No accent at all
    * Consistence phrase
    """
    
    # Fill in the placeholders in the template
    formatted_template = template.format(content=content, goal=json_schema["description"])
    
    # Generate text using the formatted template
    results = llm.generate(prompt=formatted_template,
                           json_schema=json_schema,)

    return results