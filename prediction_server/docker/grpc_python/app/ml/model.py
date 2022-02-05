from typing import ByteString
import logging
import onnxruntime as rt
from onnxGrpcServer_pb2 import Features

logging.basicConfig(level=logging.INFO)


def build_float_input(f_features):
    return [
        f_features.engines,
        f_features.passenger_capacity,
        f_features.crew,
        f_features.company_rating,
        f_features.review_scores_rating
    ]


def build_categorical_input(c_features):
    return [
        c_features.d_check_complete,
        c_features.moon_clearance_complete,
        c_features.iata_approved
    ]


class CTCVClassifier(object):
    session = None
    float_input_name = None
    categorical_input_name = None
    label_name = None

    def __init__(
        self,
        model_file_path: str = None
    ):
        logging.info("Initializing model...")
        self.model_file_path = model_file_path
        self.load_model()

    def _read_model_from_s3(self) -> ByteString:
        return self.s3_client.get_object(
            Bucket=self.s3_bucket,
            Key=self.s3_bucket)["Body"]

    def _build_session(self) -> rt.InferenceSession:
        logging.info("Fetching model file from Local...")
        logging.info(f"model_file_path: {self.model_file_path}")
        return rt.InferenceSession(self.model_file_path)

    def load_model(self) -> None:
        logging.info("Loading model...")
        logging.info("Building session...")
        self.session = self._build_session()
        logging.info("Session build Done.")
        self.float_input_name = self.session.get_inputs()[0].name
        self.categorical_input_name = self.session.get_inputs()[1].name
        self.label_name = self.session.get_outputs()[1].name
        logging.info("Model load Done.")

    def predict(self, data: Features) -> float:
        inputs = {
            self.float_input_name: [build_float_input(data.float_features)],
            self.categorical_input_name: [build_categorical_input(data.categorical_features)],
        }
        return self.session.run([self.label_name], inputs)[0][0][1]
