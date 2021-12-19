FROM python:3.7-slim-buster

RUN apt update \
    && apt install -y --no-install-recommends \
    curl wget gosu jq unzip libgomp1 python-dev default-libmysqlclient-dev python3-dev \
    apt-transport-https ca-certificates gnupg

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
    | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \
    && apt update -y && apt install -y google-cloud-sdk google-cloud-sdk-app-engine-python

ARG GCE_ACCOUNT_EMAIL
ARG GCE_PROJECT_ID

RUN gcloud config set account ${GCE_ACCOUNT_EMAIL}
RUN gcloud config set project ${GCE_PROJECT_ID}

COPY requirements.txt /tmp/
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

RUN echo "Please run 'gcloud auth login' if you want to use GCP command"
