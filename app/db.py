from typing import Annotated

from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session


DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

SessionDependency = Annotated[Session, Depends(get_session)]
