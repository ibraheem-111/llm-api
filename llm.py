from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
import os
from transformers import AutoTokenizer
import requests


class api:
    @classmethod
    def get_customer(id):
        # return '{"id":"123456", "name":"waiz", "address":"model town, lahore", "email":"waiz@mail.com", "metadata":{ "past_orders":12, "date_joined":"12-jun-2009"}}'

        url = f'{api_url}/customer'
        params = {'customer_id': id}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            customer = data.get('customer')
            return customer
        else:
            raise "the arguments were missing/invalid, or the server failed to fetch data"

    @classmethod
    def get_order(filter,value)
class Llm:
    def __init__(self):
        self.cache_dir= "./model_cache"
        self.runtimeFlag = "cuda:0"
        self.function_model_id = "Trelis/Llama-2-7b-chat-hf-function-calling-GPTQ"
        self.model_basename = "gptq_model-4bit-128g"
        self.chatting_model_id= "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
        self.extrapolation_factor = 1

    def load_models():
        os.environ["SAFETENSORS_FAST_GPU"] = "1"
        self.function_calling_model = AutoGPTQForCausalLM.from_quantized(self.function_model_id,
            model_basename=self.model_basename,
            use_safetensors=True,
            trust_remote_code=True,                                
            device="cuda:0",
            disable_exllamav2= True,
            rope_scaling = {"type": "dynamic", "factor":self.extrapolation_factor}, # allows for a max sequence length of 8192 tokens with a factor of 2.0!!!
            cache_dir=cache_dir)
        self.functionering_tokenizer = AutoTokenizer.from_pretrained(self.function_model_id, cache_dir=self.cache_dir, use_fast=True)
        
        self.chatting_model = AutoGPTQForCausalLM.from_quantized(chatting_model_id,
            # model_basename=model_basename,
            use_safetensors=True,
            trust_remote_code=True,                                
            device="cuda:0",
            # disable_exllamav2= True,
            use_triton=use_triton,
            rope_scaling = {"type": "dynamic", "factor": extrapolation_factor}, # allows for a max sequence length of 8192 tokens with a factor of 2.0!!!
            cache_dir=cache_dir)

        self.chatting_tokenizer = Autokenizer.from_pretrained(self.chatting_model_id, cache_dir = self.cache_dir, use_fast=True)
        
        if chatting_tokenizer.pad_token is None:
            chatting_tokenizer.pad_token = chatting_tokenizer.eos_token
    def setting_up_functions_for_function_calling():
        self.B_INST, self.E_INST = "[INST]", "[/INST]"
        self.B_SYS, self.E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
        
        self.api_url = "https://3dd0-103-83-89-126.ngrok-free.app"

        

