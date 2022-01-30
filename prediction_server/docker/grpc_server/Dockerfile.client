FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY ./app /app
WORKDIR /app

ENV PYTHONPATH=/app

ONBUILD ARG S3_BUCKET
ONBUILD ARG S3_BUCKET_KEY
ARG MODEL_PATH
ONBUILD ENV S3_BUCKET=${S3_BUCKET}
ONBUILD ENV S3_BUCKET_KEY=${S3_BUCKET_KEY}
ENV MODEL_PATH=${MODEL_PATH}

EXPOSE 80