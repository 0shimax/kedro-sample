import os

MODEL_PATH = os.getenv("MODEL_PATH", "pipline.onnx")
TOKEN = os.getenv("TOKEN", "1337")
S3_BUCKET = os.getenv("S3_BUCKET")
S3_BUCKET_KEY = os.getenv("S3_BUCKET_KEY")