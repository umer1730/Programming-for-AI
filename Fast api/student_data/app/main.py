from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import get_db, engine, Base
from app.models import Student
from app.schemas import StudentCreate
from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)