from fastapi import FastAPI,BackgroundTasks
from pydantic import BaseModel

from app.utils import write_log, send_email

app = FastAPI()

class LogData(BaseModel):
    message: str

class EmailData(BaseModel):
    email: str

class RegisterData(BaseModel):
    username: str
    email: str 

@app.post("/log")
def create_log(data:LogData,background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log,data.message)
    return {
        "message":"Log task added"
    }

@app.post("/send-email")
def email(data: EmailData,background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email,data.email)

    return{
        "message":"Email task added"
    }

@app.post("/register")
def register(data: RegisterData, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        write_log,
        f"New user registered: {data.username}"
        )

    background_tasks.add_task(send_email,data.email)
    return{
        "message":"User registered successfully"
    }