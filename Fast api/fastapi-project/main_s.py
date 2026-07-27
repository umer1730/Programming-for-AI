from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

Students = {
    "S001":{"name": "Ali", "marks": 95, "grade":"A+"},
    "S002":{"name": "Arslan", "marks": 80, "grade":"A"},
    "S003":{"name": "Abrar", "marks": 78, "grade":"B"},
}

# input schema
class MarksSubmission(BaseModel):
    student_id: str
    marks: int
    subject: str

@app.get("/student/{student_id:str}")
def get_student(student_id):

    if student_id not in Students:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {student_id} does't exists"
        )

    return Students[student_id]

@app.post("/submit-marks")
def submit_marks(submission: MarksSubmission):

    # error 1 students does not exists
    if submission.student_id not in Students:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {submission.student_id} does't exists"
        )

    if submission.marks < 0 and submission.marks > 100:
        raise HTTPException(
            status_code=400,
            detail={
                "error":"marks must be between 0 and 100",
                "marks_received":submission.marks,
                "fix":"enter a valid value between 0 and 100"
            }
        )

    if submission.subject.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Subject name cannot be empty"
        )

    try:
        Students[submission.student_id]["marks"] = submission.marks

        return {
            "message":"marks submitted successfully",
            "student": Students[submission.student_id]["name"],
            "subject": submission.subject,
            "marks":submission.marks
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Something went wrong to our side: {str(e)}"
        )