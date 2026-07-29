from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def get_student(name: str,age: int):
    return{
        "Name": name,
        "Age": age
    }