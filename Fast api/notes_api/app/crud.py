from sqlalchemy.orm import Session

from app.models import User, Note
from app.schemas import UserCreate, NoteCreate, NoteUpdate
from app.auth import hash_password


def create_user(db: Session, user: UserCreate):

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_username(db: Session, username: str):

    return db.query(User).filter(
        User.username == username
    ).first()

def create_note(
    db: Session,
    note: NoteCreate,
    user_id: int
):

    new_note = Note(
        title=note.title,
        content=note.content,
        owner_id=user_id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


def get_my_notes(
    db: Session,
    user_id: int
):

    return db.query(Note).filter(
        Note.owner_id == user_id
    ).all()


def get_note_by_id(
    db: Session,
    note_id: int
):

    return db.query(Note).filter(
        Note.id == note_id
    ).first()


def update_note(
    db: Session,
    note: Note,
    updated_note: NoteUpdate
):

    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note


def delete_note(
    db: Session,
    note: Note
):

    db.delete(note)
    db.commit()