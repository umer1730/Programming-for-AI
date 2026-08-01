from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.book import Book
from app.schemas.book_schema import BookCreate

router = APIRouter()


@router.post("/")
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    new_book = Book(
        title=book.title,
        author=book.author,
        price=book.price
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


@router.get("/")
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


@router.put("/{book_id}")
def update_book(
    book_id: int,
    book: BookCreate,
    db: Session = Depends(get_db)
):

    existing_book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if existing_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.price = book.price

    db.commit()
    db.refresh(existing_book)

    return existing_book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}