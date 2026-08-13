from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import joblib
from database import Base,engine,get_db
from models import Prediction
from schemas import PredictionRequest

from ml_models import(linear_model,random_forest_model,xgboost_model,neural_network_model)

#load trained models
linear_model = joblib.load("models/linear_model.joblib")
random_forest_model = joblib.load("models/random_forest_model.joblib")
xgboost_model = joblib.load("models/xgboost_model.joblib")
neural_network_model = joblib.load("models/neural_network_model.joblib")

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
        "message": "ML Prediction API is working"
    }

# prediction
@app.post("/predict")
def predict(request: PredictionRequest,db: Session = Depends(get_db)):
    input_value = request.input_value
    model_name = request.model_name.lower()

    #convert input into ml format
    X = [[input_value]]

    #select model
    if model_name == "linear":
        prediction = linear_model.predict(X)[0]

        selected_model = "LinearRegression"

    elif model_name == "random_forest":
        prediction = random_forest_model.predict(X)[0]

        selected_model = "RandomForest"

    elif model_name == "xgboost":
        prediction = xgboost_model.predict(X)[0]
        selected_model = "XGBoost"

    elif model_name == "neural_network":
        prediction = neural_network_model.predict(X)[0]
        selected_model = "NeuralNetwork"

    else:
        raise HTTPException(status_code=400,detail="Invalid model name")

    #save prediction
    new_prediction = Prediction(
        input_value = input_value,
        prediction = float(prediction),
        model_name = selected_model
    )

    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    return{
        "id": new_prediction.id,
        "input_value": input_value,
        "prediction": float(prediction),
        "model_name": selected_model
    }