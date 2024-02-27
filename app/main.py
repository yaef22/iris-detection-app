from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class FloatIn(BaseModel):
    Num_Input: float


class PredictionOut(BaseModel):
    Iris_Type: float


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: FloatIn):
    Iris_Type = predict_pipeline(payload.Num_Input)
    return {"Iris Type": Iris_Type}