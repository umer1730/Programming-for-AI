from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.teacher import Teacher
from app.schemas.teacher_schema import TeacherCreate

router = APIRouter()


@router.post("/")
def create_teacher(
    teacher: TeacherCreate,
    db: Session = Depends(get_db)
):
    new_teacher = Teacher(
        name=teacher.name,
        subject=teacher.subject,
        salary=teacher.salary
    )

    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher


@router.get("/")
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()


@router.get("/{teacher_id}")
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):

    teacher = db.query(Teacher).filter(
        Teacher.id == teacher_id
    ).first()

    if teacher is None:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return teacher


@router.put("/{teacher_id}")
def update_teacher(
    teacher_id: int,
    teacher: TeacherCreate,
    db: Session = Depends(get_db)
):

    existing_teacher = db.query(Teacher).filter(
        Teacher.id == teacher_id
    ).first()

    if existing_teacher is None:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    existing_teacher.name = teacher.name
    existing_teacher.subject = teacher.subject
    existing_teacher.salary = teacher.salary

    db.commit()
    db.refresh(existing_teacher)

    return existing_teacher


@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):

    teacher = db.query(Teacher).filter(
        Teacher.id == teacher_id
    ).first()

    if teacher is None:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    db.delete(teacher)
    db.commit()

    return {"message": "Teacher deleted successfully"}