from sqlalchemy.orm import Session
from app.models import Student
from app.schemas import StudentCreate


def create_student(db: Session, student: StudentCreate):
    new_student = Student(
        name=student.name,
        department=student.department
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


def get_students(db: Session):
    return db.query(Student).all() #Using the database connection (db), query the Student table and return all records