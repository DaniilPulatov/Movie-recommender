from fastapi import Depends


from app.ollama import OllamaClient
from app.services import EmbeddingSrv, RecommendationSrv
from app.schemas import DefaultResponse, RecommendationRequest
from app.repositories import MovieRepo
from app.core.database import new_session

from sqlalchemy.orm import Session


def get_db():
    db = new_session()
    try:
        yield db
    finally:
        db.close()
        
        
def get_movie_repo(db:Session = Depends(get_db)):
    return MovieRepo(db)

def get_emb_srv(client=OllamaClient()):
    return EmbeddingSrv(client)

def get_rec_srv(movie_repo: MovieRepo = Depends(get_movie_repo), emb_srv: EmbeddingSrv = Depends(get_emb_srv)):
    return RecommendationSrv(emb_srv, movie_repo)