from typing import Annotated

from fastapi import FastAPI, Depends, Query
from sqlmodel import SQLModel, create_engine, Session, select

from .models import Book

app = FastAPI()
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDependency = Annotated[Session, Depends(get_session)]

@app.get("/")
async def root():
    return {"Welcome!": "This is my Reading List API"}

@app.get("/books/")
async def read_books(session: SessionDependency):
    books = session.exec(select(Book))
    return books

@app.post("/books/")
async def create_book(book: Book, session: SessionDependency):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def create_books():
    book_1 = Book(title="Thinking, Fast and Slow")

    with Session(engine) as session:
        session.add(book_1)
        session.commit()
        session.refresh(book_1)
        return book_1

if __name__ == '__main__':
    create_db_and_tables()
    create_books()