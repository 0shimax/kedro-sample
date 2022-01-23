import boto3
from fastapi import status, APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

import config as config
from models import Features, PredictionResult
from prediction import Classifier
import security

clf = Classifier(
    s3_client=boto3.client("s3"),
    s3_bucket=config.S3_BUCKET,
    s3_bucket_key=config.S3_BUCKET_KEY,
    model_file_path=config.MODEL_PATH
)
api = APIRouter()

@api.post("/predict", response_model=PredictionResult)
async def post_predict(
    data: Features,
    authenticated: bool = Depends(security.validate_request),
):
    assert authenticated == True
    if not clf.session:
        raise HTTPException(status_code=500, detail="model not found")
    return clf.predict(data)

# Synchronous processing
@api.get("/update_model")
def update_model():
    clf.load_model()
    return JSONResponse(
        content={"msg": "Done!"}, 
        status_code=status.HTTP_200_OK)