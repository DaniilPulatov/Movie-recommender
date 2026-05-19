from datetime import datetime
from typing import List, Optional


from sqlalchemy.sql import func
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase

from pgvector.sqlalchemy import Vector

embedding_size = 768


'''
Reminder

Users - Ratings: one-to-many
Users - User_embeddngs: one-to-one
Movies - Ratings: one-to-many

'''


class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = "movies"
    
    id: Mapped[int] = mapped_column(primary_key=True)
     
    textual_repr: Mapped[str] = mapped_column(nullable=False)
    embedding: Mapped[list[float]] = mapped_column(Vector(embedding_size))
    
    ratings : Mapped[List["Rating"]] = relationship(back_populates="movie")
    

class Rating(Base):
    __tablename__ = "ratings"
    
    rating_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
        )
    
    user: Mapped["User"] = relationship(back_populates="ratings")
    movie: Mapped["Movie"] = relationship(back_populates="ratings")
    
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    
    ratings: Mapped[List["Rating"]] = relationship(back_populates="user")
    embedding: Mapped["UserEmbedding"] = relationship(
        back_populates="user", 
        uselist=False
        )
    
class UserEmbedding(Base):
    __tablename__ = "user_embeddings"
    
    emb_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    
    embedding: Mapped[List[float]] = mapped_column(Vector(embedding_size))
    
    user: Mapped["User"] = relationship(back_populates="embedding")
    
    

