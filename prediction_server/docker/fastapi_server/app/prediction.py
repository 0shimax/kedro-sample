from typing import ByteString
import botocore
from logging import getLogger
import onnxruntime as rt
from models import Features
from models import PredictionResult

logger = getLogger("uvicorn")

class Classifier(object):
    session = None
    float_input_name = None
    categorical_input_name = None
    label_name = None

    def __init__(
        self,
        s3_client: botocore.client.BaseClient = None,
        s3_bucket: str = None,
        s3_bucket_key: str = None,
        model_file_path: str = None
    ):
        logger.info("Initializing model...")
        self.s3_client = s3_client
        self.s3_bucket = s3_bucket
        self.s3_bucket_key = s3_bucket_key
        self.model_file_path = model_file_path
        self.load_model()

    def _read_model_from_s3(self) -> ByteString:
        return self.s3_client.get_object(
            Bucket=self.s3_bucket,
            Key=self.s3_bucket)["Body"]

    def _build_session(self) -> rt.InferenceSession:
        if self.s3_bucket:
            logger.info("Fetching model file from S3...")
            return rt.InferenceSession(self._read_model_from_s3())
        else:
            logger.info("Fetching model file from Local...")
            return rt.InferenceSession(self.model_file_path)

    def load_model(self) -> None:
        logger.info("Loading model...")
        logger.info("Building session...")
        self.session = self._build_session()
        logger.info("Session build Done.")
        self.float_input_name = self.session.get_inputs()[0].name
        self.categorical_input_name = self.session.get_inputs()[1].name
        self.label_name = self.session.get_outputs()[1].name
        logger.info("Model load Done.")

    def predict(self, data: Features) -> PredictionResult:        
        inputs = {
            self.float_input_name: Features.to_numpy(data.float_features),
            self.categorical_input_name: Features.to_numpy(data.categorical_features),
        }
        predicted = self.session.run([self.label_name], inputs)[0]
        return PredictionResult(**{"predicted": [v[1] for v in predicted]})