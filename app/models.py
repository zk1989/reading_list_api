from sqlmodel import SQLModel, Field, create_engine, Session, select


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str