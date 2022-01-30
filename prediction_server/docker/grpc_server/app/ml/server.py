from typing import List, Tuple
import asyncio
import logging

import grpc
import config
from onnxGrpcServer_pb2 import Features, UpdateParams
from onnxGrpcServer_pb2 import Predicted, Reply
from onnxGrpcServer_pb2_grpc import CTCVInferenceServicer
from onnxGrpcServer_pb2_grpc import add_CTCVInferenceServicerServicer_to_server
from model import CTCVClassifier


ctcv_classifier = CTCVClassifier(
    model_file_path=config.MODEL_PATH
)


class Classifier(CTCVInferenceServicer):
    async def predict(self, request_iterator: List[Features],
                       context: grpc.aio.ServicerContext) -> Tuple[Predicted]:
        logging.info("Serving request %s", request_iterator)
        async for request in request_iterator:
            logging.info("Serving request %s", request)
            yield Predicted(prob=ctcv_classifier.predict(request))


class ModelUpdater(CTCVInferenceServicer):
    async def update_model(self, request: UpdateParams,
                       context: grpc.ServicerContext) -> Reply:
        logging.info("Serving request %s", request)
        ctcv_classifier.load_model()
        yield Reply(status="200")


async def serve() -> None:
    server = grpc.aio.server()
    add_CTCVInferenceServicerServicer_to_server(Classifier(), server)
    add_CTCVInferenceServicerServicer_to_server(ModelUpdater(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info(f"Starting server on {listen_addr}")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())