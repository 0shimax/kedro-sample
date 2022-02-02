FROM grcp_cpp_base:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install wget
WORKDIR /root
RUN wget https://github.com/microsoft/onnxruntime/releases/download/v1.10.0/onnxruntime-linux-x64-1.10.0.tgz \
    && tar -zxvf onnxruntime-linux-x64-1.10.0.tgz

COPY ./app /app
WORKDIR /app

ARG MODEL_PATH
ENV MODEL_PATH=${MODEL_PATH}

EXPOSE 50051