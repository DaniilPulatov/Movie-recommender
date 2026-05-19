import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"
OLLAMA_MODEL = "nomic-embed-text-v2-moe"

class OllamaClient():
    def __init__(self, url:str = OLLAMA_URL, model:str =OLLAMA_MODEL):
        self.url = url
        self.model = model
    
    def __repr__(self):
        return f"Ollama Client: URL: {self.url}\tModel: {self.model}"
        
    def generate_embedding(self, repr):
        response = requests.post(
            url=self.url,
            json={
                "model": self.model,
                "prompt": repr,
            }
        )
        
        try:
            emb = response.json()["embedding"]
        except Exception as e:
            print(response.json())
            
            raise
        
        return emb