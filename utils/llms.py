import os
from dotenv import load_dotenv
from langchain_ollama  import ChatOllama

class LLMModel:
    def __init__(self, model_name="llama3.2:3b-instruct-fp16"):
        if not model_name:
            raise ValueError("Model is not defined.")
        self.model_name = model_name
        self.ChatOllama=ChatOllama(model=self.model_name)
        
    def get_model(self):
        return self.ChatOllama