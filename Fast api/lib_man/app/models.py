from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Author(Base):

    __tablename__ = "authors"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)

    books = relationship(
        "Book",
        back_populates="author"
    )

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    price = Column(Float)

    author_id = Column(Integer,ForeignKey("authors.id"))

    author = relationship(
        "Author",
        back_populates="books"
    )