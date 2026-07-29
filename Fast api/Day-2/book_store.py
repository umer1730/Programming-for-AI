from fastapi import FastAPI

app = FastAPI(title="Book store center")

books = [
    {
       "id": 1,
       "title": "Python",
       "author": "Guido",
       "price": 2000
    },
    {
       "id": 2,
       "title": "Java",
       "author": "Dev",
       "price": 1500 
    },
    {
       "id": 3,
       "title": "C++",
       "author": "John",
       "price": 1000
    },
    {
       "id": 4,
       "title": "Javascript",
       "author": "Musk",
       "price": 1800 
    },
    {
       "id": 5,
       "title": "C#",
       "author": "Mark",
       "price": 1300 
    },
]
@app.get("/")
def home():
    return{
        "message": "Welcome to the Book center"
    }

@app.get("/books")
def get_books():
    return books

@app.get("/books/{id}")
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book

    return {"message": "Book not found"}

# add a new book by query parameter
@app.post("/books")
def add_book(title:str, author:str,price:float):

    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "price": price
    }

    books.append(new_book)

    return{
        "message": "Book added Successfully",
        "book": new_book
    }

#update book (path+query)
@app.get("/books/{id}")
def update_book(id: int, title: str,author: str,price:float):
    for book in books:
        if book["id"] == id:
            book["title"] = title
            book["author"] = author
            book["price"] = price

            return{
                "message": "Book updated successfully",
                "book": book
            }

    return {"message": "Book not found"}

#Delete book
@app.delete("/books/{id}")
def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)

            return {"message": "Book deleted Successfully"}

    return {"message": "Book not found"}

# Search books by author (Query Parameter)
@app.get("/books/search")
def search_books(author: str):

    result = []

    for book in books:
        if book["author"].lower() == author.lower():
            result.append(book)

    return {
        "total_books": len(result),
        "books": result
    }