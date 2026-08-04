from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

from app.database import engine,Base,get_db
from app.models import Author, Book
from app import crud
from app.schemas import AuthorCreate,BookCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Jinnah Library")

@app.post("/authors")
def create_author(
    author: AuthorCreate,
    db: Session = Depends(get_db)
):
    return crud.create_author(db, author)

@app.get("/authors")
def get_authors(
    db: Session = Depends(get_db)
):
    return crud.get_authors(db)

@app.post("/books")
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return crud.create_book(db,book)

@app.get("/books")
def get_books(
    db: Session = Depends(get_db)
):
    return crud.get_books(db)