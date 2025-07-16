from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import create_db_and_tables


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"Welcome!": "This is my Reading List API"}
