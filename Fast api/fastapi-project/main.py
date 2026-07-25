from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first API is working"}

@app.get("/about")
def about():
    return {"project": "This model is very risky", 
            "version":"1.0"
            }