#include <iostream>
#include <string>
#include </root/onnxruntime-linux-x64-1.10.0/include/onnxruntime_cxx_api.h>

#include "build/onnxserver.pb.h"
#include "build/onnxserver.grpc.pb.h"

using onnxserver::Features;
using onnxserver::FloatData;
using onnxserver::CategoricalData;


std::vector<float> ExtractVluesFromMessageForFloat(FloatData float_data, int field_size) {
    std::vector<float> out(field_size);
    out[0] = float_data.engines();
    out[1] = float_data.passenger_capacity();
    out[2] = float_data.crew();
    out[3] = float_data.company_rating();
    out[4] = float_data.review_scores_rating();
    return out;
} 


std::vector<const char*> ExtractVluesFromMessageForCategorical(CategoricalData categorical_data, int field_size){
    std::vector<const char*> out(field_size);
    out[0] = categorical_data.d_check_complete().c_str();
    out[1] = categorical_data.moon_clearance_complete().c_str();
    out[2] = categorical_data.iata_approved().c_str();
    return out;
}


class Classifier {
public:
    Classifier(const std::string& modelPath) {
        modelPath_ = modelPath;
        LoadModel();
    }

    float Predict(Features features) {
        std::vector<float> float_input = ExtractVluesFromMessageForFloat(
            features.float_features(), float_input_dims[1]);
        std::vector<const char*> categorical_input = ExtractVluesFromMessageForCategorical(
            features.categorical_features(), categorical_input_dims[1]);
        Ort::Value float_tensor = Ort::Value::CreateTensor<float>(
            memory_info_, float_input.data(), float_input.size(), float_input_dims.data(), float_input_dims.size());
        Ort::Allocator cpu_allocator{session_,  memory_info_};
        Ort::Value categorical_tensor = Ort::Value::CreateTensor(cpu_allocator, categorical_input_dims.data(), categorical_input_dims.size(), ONNX_TENSOR_ELEMENT_DATA_TYPE_STRING);
        Ort::GetApi().FillStringTensor(static_cast<OrtValue*>(categorical_tensor), categorical_input.data(), 3U);

        Ort::Value input_tensor[] = {std::move(float_tensor), std::move(categorical_tensor)};

        auto output_tensors = session_.Run(
            Ort::RunOptions{},
            input_names.data(), input_tensor, input_names.size(),
            output_names.data(), output_names.size());

        const Ort::Value& seq_ort = output_tensors[1];
        Ort::Value map_out = seq_ort.GetValue(static_cast<int>(0), cpu_allocator);
        Ort::Value values_ort = map_out.GetValue(1, cpu_allocator);
        float* values_ret = values_ort.GetTensorMutableData<float>();
        return values_ret[1];
    };

    void LoadModel() {
        session_ = Ort::Session(env_, modelPath_.c_str(), Ort::SessionOptions{nullptr});
    }


private:
    std::string modelPath_;
    Ort::SessionOptions* session_options_;    
    Ort::Env env_ = Ort::Env{ORT_LOGGING_LEVEL_ERROR, "Default"};
    Ort::Session session_{Ort::Session{nullptr}};
    Ort::MemoryInfo memory_info_ = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);
    std::vector<const char *> input_names = {"float_input", "categorical_input"};
    std::vector<const char *> output_names = {"output_label" ,"output_probability"};
    std::vector<int64_t> float_input_dims = {1, 5};
    std::vector<int64_t> categorical_input_dims = {1, 3};
};