from pydantic import BaseModel

class PredictionInput(BaseModel):
    input_value: float

class PredictionResponse(BaseModel):
    id: int
    input_value: float
    prediction: float

    class Config:
        from_attributes = True 