from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import engine,Base,get_db
from app import crud
from app.schemas import UserCreate,TaskCreate
from app.auth import verify_password,create_access_token
from app.dependencies import get_current_user
from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

@app.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_username(
        db,
        user.username
    )
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    return crud.create_user(db,user)

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_username(
        db,form_data.username
    )
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect Password"
        )
    access_token = create_access_token(
        data={
            "sub": user.username
        }
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get("/profile")
def profile(
    current_user: User = Depends(get_db)
):
    return current_user

@app.post("/tasks")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_task(db,task,current_user.id)
# view
@app.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return crud.get_tasks(
        db,
        current_user.id
    )

#delete
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = crud.delete_task(db,task_id,current_user.id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }