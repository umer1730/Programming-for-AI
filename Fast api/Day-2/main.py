from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

#using path parameter
@app.get("/student/{student_id}/course/{course}")
def get_student(student_id: int, course: str):
    return{
        "Student_id": student_id,
        "Course": course
    }

@app.post("/student")
def create_student():
    return{
        "message": "Student created"
    }

@app.put("/student")
def update_student():
    return{
        "message": "Student Updated"
    }

@app.patch("/student")
def patch_student():
    return{
        "message": "Student Partially Updated"
    }

@app.delete("/student")
def delete_student():
    return{
        "message": "Student Deleted"
    }
