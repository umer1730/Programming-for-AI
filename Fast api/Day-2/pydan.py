from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    reg: str
    department: str = "Computer Science"
    semester: Optional[int] = None
    address: Address

@app.post("/student")
def create_student(student: Student):
    return student


