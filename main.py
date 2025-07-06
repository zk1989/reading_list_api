from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select

app = FastAPI()

class Book(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    # status: str
    # author_first_name: str | None
    # author_last_name: str
    # year: int
    # language: str
    # literature: str

DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

@app.post("/books/", response_model=Book)
def create_book(book: Book, session: Session = Depends(get_session)):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


@app.get("/")
def root():
    return {"Welcome!": "This is a Reading List API"}


@app.get("/books/", response_model=list[Book])
def get_all_books(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    books = session.exec(select(Book).offset(skip).limit(limit)).all()
    return books
