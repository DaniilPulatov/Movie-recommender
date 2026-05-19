from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    #echo=True,
    )

new_session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)