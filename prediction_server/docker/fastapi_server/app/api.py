from fastapi import APIRouter, Depends, HTTPException

from models import Features, PredictionResult
from predict import predict
from prediction import Classifier
import security

cls = Classifier()
api = APIRouter()

@api.post("/predict", response_model=PredictionResult)
async def post_predict(
    data: Features,
    authenticated: bool = Depends(security.validate_request),
):
    assert authenticated == True
    if not cls.session:
        raise HTTPException(status_code=500, detail="model not found")
    return cls.predict(data)

# Synchronous processing
@api.get("/update_model")
async def update_model():
    await cls.load_model()
