from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app import crud
from app.schemas import (
    UserCreate,
    UserResponse,
    NoteCreate,
    NoteUpdate,
    NoteResponse
)
from app.auth import verify_password, create_access_token
from app.dependencies import get_current_user
from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")


@app.post("/register", response_model=UserResponse)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = crud.get_user_by_username(
        db,
        user.username
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return crud.create_user(db, user)


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = crud.get_user_by_username(
        db,
        form_data.username
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Username"
        )

    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    token = create_access_token(
        {
            "sub": user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/profile")
def profile(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }

@app.post("/notes", response_model=NoteResponse)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return crud.create_note(
        db,
        note,
        current_user.id
    )

@app.get("/notes", response_model=list[NoteResponse])
def get_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return crud.get_my_notes(
        db,
        current_user.id
    )


@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: int,
    updated_note: NoteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    note = crud.get_note_by_id(
        db,
        note_id
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    if note.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return crud.update_note(
        db,
        note,
        updated_note
    )

@app.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    note = crud.get_note_by_id(
        db,
        note_id
    )

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    if note.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    crud.delete_note(
        db,
        note
    )

    return {
        "message": "Note deleted successfully"
    }