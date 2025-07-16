from sqlmodel import SQLModel, Field


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
