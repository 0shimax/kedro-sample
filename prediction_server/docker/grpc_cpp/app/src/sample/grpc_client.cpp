#include <iostream>
#include <grpcpp/security/credentials.h>
#include <grpcpp/create_channel.h>
#include "build/sample.pb.h"
#include "build/sample.grpc.pb.h"

int main(int argc, char **argv) {
  std::cout << "Hello, World! I'm simple client" << std::endl;
  if (argc < 2){
    std::cout << "Must input 2 args" << std::endl;
    return 0;
  }
  auto str1 = argv[1];
  auto str2 = argv[2];

  auto channel = grpc::CreateChannel("localhost:50051",
                                     grpc::InsecureChannelCredentials());
  auto stub = simple::Add::NewStub(channel);

  simple::AddRequest req;
  req.set_str1(str1);
  req.set_str2(str2);

  grpc::ClientContext ctx;
  simple::AddReply res;
  auto status = stub->Add(&ctx, req, &res);
  if (!status.ok()) {
    std::cout << status.error_code() << ": " << status.error_message() << std::endl;
    std::cout <<  "RPC failed" << std::endl;
    return 0;
  }
  std::cout << "[Client] ReceivedRes: " << res.str() << std::endl;
  return 0;
}