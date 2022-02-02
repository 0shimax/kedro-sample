#include <iostream>
#include <grpcpp/ext/proto_server_reflection_plugin.h>
#include <grpcpp/grpcpp.h>
#include "build/sample.pb.h"
#include "build/sample.grpc.pb.h"

namespace simple {
class SimpleAddImpl final : public Add::Service {
  ::grpc::Status Add(::grpc::ServerContext *context, const AddRequest *req, AddReply *res) override {
    std::cout << "[Server] ReceivedReq: " << req->str1() << ", " << req->str2() << std::endl;
    res->set_str(req->str1() + req->str2());
    return ::grpc::Status::OK;
  }
};
};

void RunServer() {
  std::string server_address("localhost:50051");
  simple::SimpleAddImpl service_simple;

  grpc::EnableDefaultHealthCheckService(true);
  grpc::reflection::InitProtoReflectionServerBuilderPlugin();
  grpc::ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service_simple);

  std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;
  server->Wait();
}

int main(int argc, char **argv) {
  std::cout << "Hello, World! server" << std::endl;
  RunServer();
  return 0;
}