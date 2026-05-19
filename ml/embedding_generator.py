from typing import List

from app.ollama import OllamaClient
from app.core import database
from app.models import Movie
from app.repositories import MovieRepo
from app.services import EmbeddingSrv
from ml.preprocessing import DataLoader

import sys


#path_to_dataset = "netflix_titles.csv"
movie_reprs = DataLoader().get_movie_repr()

ollama_client = OllamaClient()

emb_srv = EmbeddingSrv(client=ollama_client)

movie_repo = MovieRepo(db=database.new_session())



BATCH_SIZE = 100
batch = []

for i, repr in enumerate(movie_reprs):
    embedding = emb_srv.embeed_text(repr)
    
    batch.append(
        Movie(textual_repr=repr, embedding=embedding)
        )
    
    if len(batch) == BATCH_SIZE:
        # TO DO: Save embedding to database
        movie_repo.batch_save(batch)
        batch.clear()
        
        print(f" Batches Procecced: {i+1}")
        

print("Movies are loaded")