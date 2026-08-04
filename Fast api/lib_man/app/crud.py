from sqlalchemy.orm import Session
from app.models import Author,Book
from app.schemas import AuthorCreate, BookCreate

def create_author(db: Session,author: AuthorCreate):
    new_author = Author(name = author.name)

    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    return new_author

def get_authors(db: Session):
    return db.query(Author).all()

def create_book(db: Session, book: BookCreate):
    new_book = Book(
        title = book.title,
        price = book.price,
        author_id = book.author_id
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

def get_books(db: Session):
    return db.query(Book).all()