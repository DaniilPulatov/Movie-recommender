
from app.ollama import OllamaClient

from typing import List

from app.repositories import MovieRepo
from app.schemas import RecommendationResponse

class EmbeddingSrv():
    def __init__(self, client: OllamaClient):
        self.client = client
        
    def embeed_text(self, text:str) -> list[float]:
        return self.client.generate_embedding(text)

class RecommendationSrv():
    def __init__(self, emb_srv: EmbeddingSrv, movie_repo: MovieRepo):
        
        self.emb_srv = emb_srv
        self.movie_repo = movie_repo
    
    def recommend(self, query:str, K:int=10) -> List:
        """
        Flow:
        1. Generate query embedding
        2. Make request to database to extract K most simillar to query
        3. Return K records
        """
        q_embedding = self.emb_srv.embeed_text(text=query)
        movies = self.movie_repo.get_similar_movies(q_embedding, K)
        
        return [
            RecommendationResponse.model_validate(movie)
            for movie in movies
        ]
        