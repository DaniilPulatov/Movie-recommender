from typing import List

from sqlalchemy.orm import Session

from sqlalchemy import select
# from pgvector.sqlalchemy import cosine_distance

from app.models import Movie

class MovieRepo():
    def __init__(self, db: Session):
        self.db = db
        
    def batch_save(self, movies: List) -> None:
        self.db.add_all(movies)
        self.db.commit()
    
    def get_similar_movies(self, query_embedding: list[float], limit: int = 10):

        stmt = (
            select(Movie).order_by(Movie.embedding.cosine_distance(query_embedding)).limit(limit)
            #.order_by(cosine_distance(Movie.embedding, query_embedding))
            #.limit(limit)
        )
        result = self.db.scalars(stmt).all()
        
        return result
    

    