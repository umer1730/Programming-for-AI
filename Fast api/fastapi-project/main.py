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

@app.get("/customer")
def get_customer(customer_id: int):
    return {
        "customer_id":customer_id,
        "name":"Ali",
        "status":"active"
    }