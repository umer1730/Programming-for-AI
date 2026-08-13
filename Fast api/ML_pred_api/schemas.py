from pydantic import BaseModel

class PredictionRequest(BaseModel):
    input_value: float
    model_name: str

class PredictionResponse(BaseModel):
    id: int
    input_value: float
    prediction: float
    model_name: str

    class Config:
        from_attributes = True 