from fastapi import APIRouter, Depends

from models import Features, PredictionResult
from predict import predict
import security

api = APIRouter()

@api.post("/predict", response_model=PredictionResult)
async def post_predict(
    data: Features,
    authenticated: bool = Depends(security.validate_request),
):
    assert authenticated == True
    return predict(data)
