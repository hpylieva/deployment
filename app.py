from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import json
import numpy as np

app = FastAPI(
    title="Iris Classification API", 
    description="API for classifying iris flowers using ML"
)

# Load the trained model and target names
model = joblib.load('model/model.joblib')
with open('model/target_names.json', 'r') as f:
    target_names = json.load(f)

class PredictionRequest(BaseModel):
    features: List[float]
    
    class Config:
        schema_extra = {
            "example": {
                "features": [5.1, 3.5, 1.4, 0.2]
            }
        }

class PredictionResponse(BaseModel):
    class_name: str
    
    class Config:
        schema_extra = {
            "example": {
                "class_name": "setosa"
            }
        }

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API!"
            "This is a simple API for classifying iris flowers using ML."}

@app.post("/predict/", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    features = np.array(request.features).reshape(1, -1)
    prediction = model.predict(features)
    class_name = target_names[prediction[0]]
    return PredictionResponse(class_name=class_name) 