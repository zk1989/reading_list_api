from typing import Annotated

from fastapi import FastAPI, Depends, Query
from sqlmodel import SQLModel, create_engine, Session, select

from .models import Book

app = FastAPI()


DATABASE_URL = "sqlite:///books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]



@app.get("/")
async def root():
    return {"Welcome!": "This is my Reading List API"}

@app.get("/books/", response_model=list[Book])
async def read_books(session: SessionDep,
               limit: Annotated[int, Query(le=10)] = 10):
    books = session.exec(select(Book).limit(limit)).all()
    return books

@app.post("/books/", response_model=Book)
async def create_book(book: Book, session: SessionDep):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def create_books():
    book_1 = Book(title="Thinking, Fast and Slow")

    with Session(engine) as session:
        session.add(book_1)
        session.commit()
