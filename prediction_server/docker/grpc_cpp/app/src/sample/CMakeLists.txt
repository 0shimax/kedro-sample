cmake_minimum_required(VERSION 3.18.4)

project(grpc_test)

include(../../cmake/common.cmake)

# Proto file
get_filename_component(proto "../../protos/sample.proto" ABSOLUTE)
get_filename_component(proto_path "${proto}" PATH)

# Generated sources
set(proto_srcs "${CMAKE_CURRENT_BINARY_DIR}/sample.pb.cc")
set(proto_hdrs "${CMAKE_CURRENT_BINARY_DIR}/sample.pb.h")
set(grpc_srcs "${CMAKE_CURRENT_BINARY_DIR}/sample.grpc.pb.cc")
set(grpc_hdrs "${CMAKE_CURRENT_BINARY_DIR}/sample.grpc.pb.h")
add_custom_command(
      OUTPUT "${proto_srcs}" "${proto_hdrs}" "${grpc_srcs}" "${grpc_hdrs}"
      COMMAND ${_PROTOBUF_PROTOC}
      ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}"
        --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
        -I "${proto_path}"
        --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
        "${proto}"
      DEPENDS "${proto}")

# Include generated *.pb.h files
include_directories("${CMAKE_CURRENT_BINARY_DIR}")

# grpc_proto
add_library(grpc_proto
  ${grpc_srcs}
  ${grpc_hdrs}
  ${proto_srcs}
  ${proto_hdrs})
target_link_libraries(grpc_proto
  ${_REFLECTION}
  ${_GRPC_GRPCPP}
  ${_PROTOBUF_LIBPROTOBUF})

# Targets greeter_[async_](client|server)
foreach(_target grpc_client grpc_server)
  add_executable(${_target} "${_target}.cpp")
  target_link_libraries(${_target}
    grpc_proto
    ${_REFLECTION}
    ${_GRPC_GRPCPP}
    ${_PROTOBUF_LIBPROTOBUF})
endforeach()