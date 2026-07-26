from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    age: int
    income: float
    loan_amount: float
    employment_years: int

@app.post("/predict")
def predict_loan(application: LoanApplication):

    if application.income > 60000 and application.employment_years > 3:
        decision = "approved"

    else:
        decision = "rejected"

    return {
        "application_age": application.age,
        "decision":decision
    }