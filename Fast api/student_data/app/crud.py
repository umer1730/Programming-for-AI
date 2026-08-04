from sqlalchemy.orm import Session
from app.models import Student
from app.schemas import StudentCreate


def create_student(db: Session, student: StudentCreate):
    new_student = Student(
        name=student.name,
        department=student.department,
        age=student.age,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


def get_students(db: Session):
    return db.query(Student).all() #Using the database connection (db), query the Student table and return all records

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(
        Student.id == student_id
    ).first()

def update_student(db: Session,student_id: int,student: StudentCreate):
    db_student = get_student(db,student_id)
    if db_student is None:
        return None

    db_student.name = student.name
    db_student.department = student.department

    db.commit()
    db.refresh(db_student)

    return db_student

def delete_student(db: Session,student_id: int):
    student = get_student(db,student_id)
    if student is None:
        return None

    db.delete(student)
    db.commit()

    return student 