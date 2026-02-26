import sqlmodel
from sqlmodel import SQLModel, Field, Session
from sqlalchemy import text
from .config import DATABASE_URL

engine = sqlmodel.create_engine(DATABASE_URL, echo=True)

def init_db():
    with engine.begin() as conn:
        conn.execute(text("SELECT pg_advisory_lock(1)"))
        SQLModel.metadata.create_all(engine)
        conn.execute(text("SELECT pg_advisory_unlock(1)"))

def get_session():
    with Session(engine) as session:
        yield session