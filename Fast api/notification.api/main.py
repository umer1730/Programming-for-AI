from fastapi import FastAPI,BackgroundTasks

from schemas import UserCreate
from background import (save_log,send_welcome_email,create_notification)

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Notification API is running"
    }

@app.post("/register")
def register(user: UserCreate,background_tasks: BackgroundTasks):
    background_tasks.add_task(save_log,user.name,user.email)

    #background task 2
    background_tasks.add_task(send_welcome_email,user.email)

    #background task 3
    background_tasks.add_task(create_notification,user.name)

    return{
        "message":"Registration successful",
        "name": user.name,
        "email": user.email
    }