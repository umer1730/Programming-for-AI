from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app  = FastAPI(title="Library Management System")

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    pages: Optional[int] = None
    available: bool = True

books = []

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return{
        "message": "Book added successfully",
        "book": book
    }

#get books
@app.get("/books")
def get_books():
    return books

# get book by id
@app.get("/books/{id}")
def get_book(id: int):
    for book in books:
        if book.id == id:
            return book

    return {
        "message": "Book not found"
    }