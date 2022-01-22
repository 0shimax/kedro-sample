import boto3
import onnxruntime as rt
from models import Features
from models import PredictionResult
import config as config


class Classifier(object):
    session = None
    float_input_name = None
    categorical_input_name = None
    label_name = None
    s3_client = boto3.client("s3")

    def __init__(self):
        self.load_model()

    def _read_model_from_s3(self):
        return self.s3_client.get_object(
            Bucket=config.S3_BUCKET,
            Key=config.S3_BUCKET_KEY)["Body"]

    def load_model(self):
        self.session = rt.InferenceSession(self._read_model_from_s3())
        self.float_input_name = self.session.get_inputs()[0].name
        self.categorical_input_name = self.session.get_inputs()[1].name
        self.label_name = self.session.get_outputs()[1].name

    def predict(self, data: Features) -> PredictionResult:        
        inputs = {
            self.float_input_name: Features.to_numpy(data.float_features),
            self.categorical_input_name: Features.to_numpy(data.categorical_features),
        }
        predicted = self.session.run([self.label_name], inputs)[0]
        return PredictionResult(**{"predicted": [v[1] for v in predicted]})