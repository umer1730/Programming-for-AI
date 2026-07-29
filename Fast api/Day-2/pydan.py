from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    reg: str
    department: str = "Computer Science"
    semester: Optional[int] = None

@app.post("/student")
def create_student(student: Student):
    return student


