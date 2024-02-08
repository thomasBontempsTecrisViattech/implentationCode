from implentationCode.HuggingFaceLLM import HuggingFaceLLM

def extract_structured_data(content: str, json_schema):
    llm = HuggingFaceLLM(temperature=0)  # Choose the desired Hugging Face model
    
    template = """
    The resume is below and delimited by --START-- and --END--. You will use this resume to extract the information. 
    Your role is to have an recruiter point of vue to permit of respond the best at the json schema.
    
    --START--

    {content}
    
    --END--
    
    """
    
    # Fill in the placeholders in the template
    formatted_template = template.format(content=content)#, data_points=data_points)
    print("\n\nformatted_template : " + formatted_template + "\n\n")
    
    # Generate text using the formatted template
    
    
    results = llm.generate(prompt=formatted_template,
                           json_schema=json_schema)

    return results