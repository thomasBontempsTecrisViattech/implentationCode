import torch
import os

from transformers import AutoTokenizer, AutoModelForCausalLM
from jsonFormer.jsonformer.main import Jsonformer

#os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
torch.cuda.empty_cache() 
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:512"

class HuggingFaceLLM:
    # Model_name : databricks/dolly-v2-3b, 
    def __init__(self, model_name="databricks/dolly-v2-7b"):
        self.model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        

    def generate(self, prompt, json_schema, temperature=0.0001):# strictly positive
        #device = "cuda:0" if torch.cuda.is_available() else "cpu"
        device = 'cpu'
        builder = Jsonformer(
            model=self.model,
            tokenizer=self.tokenizer,
            json_schema=json_schema,
            prompt= prompt,
            temperature=temperature,
            device=device
        )

        

        print("Generating...")
        output = builder()
        #highlight_values(output)
        return output