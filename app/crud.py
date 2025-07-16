from sqlmodel import Session, select
from app.models import Book


def read_books(session: Session):
    books = session.exec(select(Book)).all()
    return books

def create_book(book: Book, session: Session):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book
