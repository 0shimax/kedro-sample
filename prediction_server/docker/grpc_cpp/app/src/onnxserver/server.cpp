#include <iostream>
#include <string>
#include <vector>
#include <memory>

#include <grpc/support/log.h>
#include <grpcpp/grpcpp.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>

#include "build/onnxserver.pb.h"
#include "build/onnxserver.grpc.pb.h"
#include "classifier.cpp"

using grpc::Server;
using grpc::ServerReaderWriter;
using grpc::ServerBuilder;
using grpc::ServerCompletionQueue;
using grpc::ServerContext;
using grpc::Status;
using grpc::EnableDefaultHealthCheckService;
using grpc::reflection::InitProtoReflectionServerBuilderPlugin;
using onnxserver::CTCVInferenceServicer;
using onnxserver::Predicted;
using onnxserver::Features;
using onnxserver::UpdateParams;
using onnxserver::Reply;


class ServiceImpl final : public CTCVInferenceServicer::Service {
    Status Predict(ServerContext* context,
                ServerReaderWriter<Predicted, Features>* stream) override {
        Features request;
        while (stream->Read(&request)) {
            float predicted;            
            try {
                predicted = classifier.Predict(request);
            }
            catch (Ort::Exception& e) {
                std::cout << e.what() << std::endl;
                return Status::CANCELLED;
            }
            Predicted reply;
            reply.set_prob(predicted);
            stream->Write(reply);
        }
        return Status::OK;
    }
    Status UpdateModel(ServerContext* context, const UpdateParams* request,
                    Reply* reply) override {
        try {
            classifier.LoadModel();
            reply->set_status("200");
            return Status::OK;
        }
        catch(...) {
            std::cerr << "Failed loading model" << std::endl;
            reply->set_status("500");
            return Status::CANCELLED;
        }
    }

    private:
        Classifier classifier{"/models/pipeline.onnx"};
};

void RunServer() {
    std::string server_address("0.0.0.0:50051");
    ServiceImpl service;

    EnableDefaultHealthCheckService(true);
    InitProtoReflectionServerBuilderPlugin();
    ServerBuilder builder;
    // Listen on the given address without any authentication mechanism.
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    // Register "service" as the instance through which we'll communicate with
    // clients. In this case it corresponds to an *synchronous* service.
    builder.RegisterService(&service);
    // Finally assemble the server.
    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;

    // Wait for the server to shutdown. Note that some other thread must be
    // responsible for shutting down the server for this call to ever return.
    server->Wait();
}

int main(int argc, char** argv) {
    RunServer();
    return 0;
}