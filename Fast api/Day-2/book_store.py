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
def get_book():
    return{
        "message": "Welcome to the Book center"
    }

@app.get("/books")
def get_book():
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