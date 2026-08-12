from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

from database import Base,engine,get_db
from models import Prediction
from schemas import PredictionInput,PredictionResponse

#create database table
Base.metadata.create_all(bind=engine)

app = FastAPI(title = "ML Predictions API")
#ml prediction function
def predict_value(input_value: float):
    prediction = input_value * 2
    return prediction 

@app.get("/")
def home():
    return{
        "message": "ML Prediction API is running"
    }

@app.post("/predict",response_model=PredictionResponse)
def predict(data: PredictionInput,db: Session = Depends(get_db)):
#ml prediction
    result = predict_value(data.input_value)

#database object
    new_prediction = Prediction(
        input_value = data.input_value,
        prediction = result)

    #save to database
    db.add(new_prediction)

    db.commit()
    db.refresh(new_prediction)

    return new_prediction
