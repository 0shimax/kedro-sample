import asyncio
import logging

import grpc
from hellostreamingworld_pb2 import HelloReply
from hellostreamingworld_pb2 import HelloRequest
from hellostreamingworld_pb2_grpc import MultiGreeterServicer
from hellostreamingworld_pb2_grpc import add_MultiGreeterServicer_to_server

NUMBER_OF_REPLY = 10


class Greeter(MultiGreeterServicer):

    async def sayHello(self, request: HelloRequest,
                       context: grpc.aio.ServicerContext) -> HelloReply:
        logging.info("Serving sayHello request %s", request)
        for i in range(NUMBER_OF_REPLY):
            yield HelloReply(message=f"Hello number {i}, {request.name}!")


async def serve() -> None:
    server = grpc.aio.server()
    add_MultiGreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())