FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY ./app /app
WORKDIR /app

ENV PYTHONPATH=/app

COPY models/pipeline.onnx /tmp/pipeline.onnx
ENV MODEL_PATH=/tmp/pipeline.onnx

ARG S3_BUCKET
ARG S3_BUCKET_KEY
ENV S3_BUCKET=${S3_BUCKET}
ENV S3_BUCKET_KEY=${S3_BUCKET_KEY}

EXPOSE 80