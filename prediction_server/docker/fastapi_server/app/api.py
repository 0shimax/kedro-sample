from fastapi import APIRouter, Depends
from logging import getLogger

from models import Features, FloatFeatures, CategoricalFeatures, PredictionResult
from predict import predict
import security

api = APIRouter()
logger = getLogger(__name__)

@api.post("/predict", response_model=PredictionResult)
def post_predict(
    data: Features,
    authenticated: bool = Depends(security.validate_request),
):
    logger.info(data)
    assert authenticated == True
    return predict(data)
    # return predict(float_features, categorical_features)