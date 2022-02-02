#include <iostream>
#include <thread>
#include <chrono>
#include <grpc/support/log.h>
#include <grpcpp/grpcpp.h>

#include "build/onnxserver.pb.h"
#include "build/onnxserver.grpc.pb.h"

using grpc::Channel;
using grpc::ClientReaderWriter;
using grpc::ClientContext;
using grpc::CompletionQueue;
using grpc::Status;
using onnxserver::CTCVInferenceServicer;
using onnxserver::Predicted;
using onnxserver::Features;
using onnxserver::FloatData;
using onnxserver::CategoricalData;
using onnxserver::UpdateParams;
using onnxserver::Reply;


FloatData MakeFloatData(
  float engines,
  float passenger_capacity,
  float crew,
  float company_rating,
  float review_scores_rating
) {
  FloatData falotFeatures;
  falotFeatures.set_engines(engines);
  falotFeatures.set_passenger_capacity(passenger_capacity);
  falotFeatures.set_crew(crew);
  falotFeatures.set_company_rating(company_rating);
  falotFeatures.set_review_scores_rating(review_scores_rating);
  return falotFeatures;
}

CategoricalData MakeCategoricalData(
  std::string d_check_complete,
  std::string moon_clearance_complete,
  std::string iata_approved
) {
  CategoricalData categoricalData;
  categoricalData.set_d_check_complete(d_check_complete);
  categoricalData.set_moon_clearance_complete(moon_clearance_complete);
  categoricalData.set_iata_approved(iata_approved);
  return categoricalData;
}

Features MakeFeaures(
  float engines,
  float passenger_capacity,
  float crew,
  float company_rating,
  float review_scores_rating,
  std::string d_check_complete,
  std::string moon_clearance_complete,
  std::string iata_approved
) {
  Features f;
  FloatData float_features = MakeFloatData(engines, passenger_capacity, crew, company_rating, review_scores_rating);
  CategoricalData categorical_features = MakeCategoricalData(d_check_complete, moon_clearance_complete, iata_approved);
  f.mutable_float_features()->CopyFrom(float_features);
  f.mutable_categorical_features()->CopyFrom(categorical_features);
  return f;
}


int main(int argc, char **argv) {
  auto channel = grpc::CreateChannel("localhost:50051",
                                     grpc::InsecureChannelCredentials());
  auto stub = CTCVInferenceServicer::NewStub(channel);

  grpc::ClientContext ctx;
  std::shared_ptr<ClientReaderWriter<Features, Predicted> > stream(
        stub->Predict(&ctx));
  
  std::chrono::system_clock::time_point start, end;
  start = std::chrono::system_clock::now();
  std::thread writer([stream]() {
    std::vector<Features> features{
      MakeFeaures(2.0,4.0,3.0,1.0,96.0, "False", "False", "True"),
      MakeFeaures(4.0,8.0,5.0,1.0,100.0, "True", "False", "False"),
      MakeFeaures(2.0,4.0,3.0,1.0,96.0, "False", "False", "True"),
      MakeFeaures(4.0,8.0,5.0,1.0,100.0, "True", "False", "False"),
      MakeFeaures(2.0,4.0,3.0,1.0,96.0, "False", "False", "True"),
      MakeFeaures(4.0,8.0,5.0,1.0,100.0, "True", "False", "False"),
      MakeFeaures(2.0,4.0,3.0,1.0,96.0, "False", "False", "True"),
      MakeFeaures(4.0,8.0,5.0,1.0,100.0, "True", "False", "False"),
      MakeFeaures(2.0,4.0,3.0,1.0,96.0, "False", "False", "True"),
      MakeFeaures(4.0,8.0,5.0,1.0,100.0, "True", "False", "False")
    };
    for (const Features& feature : features) {
      stream->Write(feature);
    }
    stream->WritesDone();
  });
  
  Predicted res;
  while (stream->Read(&res)) {
    std::cout << "Got response " << res.prob() << std::endl;
    res.prob();
  }
  writer.join();  
  Status status = stream->Finish();
  end = std::chrono::system_clock::now();
  double time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
  std::cout << "net time[ms]: " << time << std::endl;

  if (!status.ok()) {
    std::cout << "Predict rpc failed." << std::endl;
    return 0;
  }
}