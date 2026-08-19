from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate


app =FastAPI()
@app.get("/")
def home():
    return {
        "message":"Fastapi + PostgreSQL"
    }

@app.post("/users")
def create_user(user:UserCreate,db: Session = Depends(get_db)):
    new_user=User(name = user.name,
                  email = user.email,
                  age = user.age
                  )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users")
def get_user(db:Session = Depends(get_db)):
    users = db.query(User).all()

    return users
