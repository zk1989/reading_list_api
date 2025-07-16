from fastapi import APIRouter

from app.crud import read_books, create_book
from app.db import SessionDependency
from app.models import Book


router = APIRouter()

@router.get("/books/", response_model=list[Book])
def get_books(session: SessionDependency):
    return read_books(session)

@router.post("/books/", response_model=Book)
def add_book(book: Book, session: SessionDependency):
    return create_book(book, session)
