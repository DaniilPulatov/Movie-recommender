from abc import abstractmethod
from typing import List, Optional, Protocol

from app.models import Movie, Rating

class MovieInterface(Protocol):
    # @abstractmethod
    # def get_by_id(self, movie_id) -> Optional[Movie]: ... 
    
    # @abstractmethod
    # def create(self, movie) -> None: ...
    
    @abstractmethod
    def select_simillar(self, K) -> List[Movie]: ...
    
    @abstractmethod
    def bulk_save(self, movies: List): ...
    
    
    
class UserInterface(Protocol):
    @abstractmethod
    def create(self, user) -> None: ...
    
    
class RatingInterface(Protocol):
    @abstractmethod
    def get_by_user_id(self, user_id) -> List[Rating]: ... 
    
    @abstractmethod
    def get_by_movie_id(self, user_id) -> List[Rating]: ... 
    
    @abstractmethod
    def create(self, rating) -> None: ... 
    

class UserEmbeddingInterface(Protocol):
    def get_by_user_id(self, user_id): ...
    def upsert_embedding(self, user_id, vector): ...