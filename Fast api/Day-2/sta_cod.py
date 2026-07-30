from fastapi import FastAPI,status,HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return{
        "message":"Welcome"
    }

@app.post("/student", status_code=status.HTTP_201_CREATED)
def create_student():
    return{
        "message":"Student created"
    }

#but now using HTTPException
@app.get("/student/{id}")
def get_student(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": 1,
        "name": "Ali"
    }

#multiple error conditions
@app.get("/marks/{marks}")
def get_marks(marks: int):
    if marks < 0:
        raise HTTPException(
            status_code=400,
            detail="Marks cannot be negative"
        )

    if marks > 100:
        raise HTTPException(
            status_code=400,
            detail="Marks cannot exceeded 100"
        ) 

    return{
        "marks": marks
    }


#JSONResponse
@app.get("/success")
def success():
    return JSONResponse(
        status_code=200,
        content={
            "message":"Everything is working"
        }
    )

#responses with custom data
@app.get("/profile")
def profile():
    return JSONResponse(
        status_code=200,
        content={
            "id":1,
            "name":"Ali",
            "department":"CS"
        }
    )

#raising different exceptions
@app.get("/login")
def login():
    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )

@app.get("/admin")
def admin():
    raise HTTPException(
        status_code=403,
        detail="Access denied"
    )

# internal server error
@app.get("/server")
def server():
    raise HTTPException(
        status_code=500,
        detail="Internal Server Error"
    )

