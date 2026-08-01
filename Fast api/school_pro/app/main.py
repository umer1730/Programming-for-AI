from fastapi import FastAPI
from .routers import students,teachers,books
from app.database import engine, Base
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.book import Book

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    students.router,
    prefix="/students",
    tags=["Students"]
)

app.include_router(
    teachers.router,
    prefix="/teachers",
    tags=["Teachers"]
)

app.include_router(
    books.router,
    prefix="/books",
    tags=["Books"]
)

@app.get("/")
def home():
    return {"message":"Welcome To School Management"}
