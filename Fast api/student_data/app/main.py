from fastapi import FastAPI, Depends,HTTPException
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

@app.get("/students/{student_id}")
def read_student(student_id: int,db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@app.put("/students/{studnet_id}")
def update(student_id: int,student: StudentCreate,db: Session = Depends(get_db)):

    updated = crud.update_student(db,student_id,student)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return updated

@app.delete("/students/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db,student_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }