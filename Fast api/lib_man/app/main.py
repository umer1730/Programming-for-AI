from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session

from app.database import engine,Base,get_db
from app.models import Author, Book
from app import crud
from app.schemas import AuthorCreate,BookCreate,AssignAuthor

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Jinnah Library System")

@app.get("/")
def home():
    return{
        "message": "Welcome to Jinnah Library Sytem!"
    }
@app.post("/books")
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return crud.create_book(db,book)

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

@app.post("/assign-author")
def assign_author(
    data: AssignAuthor,
    db: Session = Depends(get_db)
):
    result = crud.assign_author(
        db,
        data.book_id,
        data.author_id
    )
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book or Author not found"
        )
    return{
        "message": "Author assigned successfully"
    }

@app.get("/books")
def get_books(
    db: Session = Depends(get_db)
):
    return crud.get_books(db)

@app.get("/authors")
def get_authors(
    db: Session = Depends(get_db)
):
    return crud.get_books(db)