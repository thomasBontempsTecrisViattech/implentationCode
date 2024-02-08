from transformers import AutoTokenizer, AutoModelForCausalLM
from jsonFormer.jsonformer.main import Jsonformer

class HuggingFaceLLM:
    # Model_name : databricks/dolly-v2-3b, 
    def __init__(self, 
                 model_name="databricks/dolly-v2-3b"):
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        

    def generate(self, prompt, json_schema, temperature=0.0):

        builder = Jsonformer(
            model=self.model,
            tokenizer=self.tokenizer,
            json_schema=json_schema,
            prompt= prompt,
            temperature=temperature,
        )

        

        print("Generating...")
        output = builder()
        #highlight_values(output)
        return output