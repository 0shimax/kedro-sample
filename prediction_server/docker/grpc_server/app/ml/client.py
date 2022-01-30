import asyncio
import logging

import grpc
from onnxGrpcServer_pb2 import Features, UpdateParams
from onnxGrpcServer_pb2_grpc import CTCVInferenceServicerStub
import input_data
import time


async def request(stub, payloads):
    start = time.time()
    responses = stub.predict(iter(payloads))
    while True:
        response = await responses.read()
        if response == grpc.aio.EOF:
            break
        # print(f"responce: {response.prob}")
    print(time.time() - start)

async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = CTCVInferenceServicerStub(channel)
        payloads = []
        for i in range(10):
            payloads.append(Features(**input_data.features_one[i%2]))
        await request(stub, payloads)


async def update():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = CTCVInferenceServicerStub(channel)
        res = stub.update_model(UpdateParams(param="updating"))
        while True:
            response = await res
            if response == grpc.aio.EOF:
                break
        print(res)

if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
    # asyncio.run(update())