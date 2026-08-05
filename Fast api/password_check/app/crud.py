from sqlalchemy.orm import Session

from app.models import User,Task
from app.schemas import (
    UserCreate,
    TaskCreate
)

from app.auth import hash_password
def get_user_by_username(
        db: Session,
        username: str
):
    return db.query(User).filter(
        User.username == username
    ).first()

def create_user(
        db:Session,
        user:UserCreate
):
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def create_task(
        db:Session,
        task: TaskCreate,
        owner_id: int
        ):
    new_task = Task(
        title= task.title,
        owner_id=owner_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_tasks(
    db: Session,
    owner_id: int
):
    return db.query(Task).filter(
        Task.owner_id == owner_id
    ).all()

def delete_task(
    db:Session,
    task_id: int,
    owner_id: int
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == owner_id
    ).first()

    if task is None:
        return None

    db.delete(task)
    db.commit()
    return task