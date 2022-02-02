# HOW TO USE
# If you want to generate protobuf/grpc cpp files for the following proto files
# ```
# <your project root>
# ├── CMakeLists.txt
# ├── cmake
# │   └── GRPCHelper.cmake
# ├── protos
# │   ├── p1.proto
# │   └── p2.proto
# └── src
#     ├── CMakeLists.txt
#     ├── client.cpp
#     └── server.cpp
# ```
#
# you should like this in your CMakeLists.txt in `src`
# ```
# find_package(gRPC CONFIG REQUIRED)
# find_package(Protobuf CONFIG REQUIRED)
# include(${CMAKE_SOURCE_DIR}/cmake/GRPCHelper)
# pb_grpc_generate_cpp(PROTO_SRCS PROTO_HDRS GRPC_SRCS GRPC_HDRS ${CMAKE_SOURCE_DIR}/protos/p1.proto ${CMAKE_SOURCE_DIR}/protos/p2.proto)
# add_library(grpc_proto ${PROTO_SRCS} ${PROTO_HDRS} ${GRPC_SRCS} ${GRPC_HDRS})
# target_link_libraries(grpc_proto gRPC::grpc++ protobuf::libprotobuf gRPC::grpc++_reflection)
# foreach (_target server client)
#   add_executable(${_target} "${CMAKE_CURRENT_SOURCE_DIR}/${_target}.cpp")
#   target_link_libraries(${_target} grpc_proto ${_REFLECTION} ${_GRPC_GRPCPP} ${_PROTOBUF_LIBPROTOBUF})
# endforeach ()
# ```

function(pb_grpc_generate_cpp PROTO_SRCS PROTO_HDRS GRPC_SRCS GRPC_HDRS)
    set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)
    set(_GRPC_CPP_PLUGIN_EXE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)

    foreach (_protopath ${ARGN})
        get_filename_component(_protoname ${_protopath} NAME_WE)
        get_filename_component(${_protoname}_PROTOFILE ${_protopath} ABSOLUTE)
        get_filename_component(${_protoname}_PROTOFILE_DIR "${${_protoname}_PROTOFILE}" DIRECTORY)

        # CMAKE_CURRENT_BINARY_DIR is only acceptable for the output directory
        # https://stackoverflow.com/questions/32715225/cmakelist-to-generate-cc-and-h-files-from-proto-file-under-a-specific-folder/32721897
        set(${_protoname}_PROTO_SRCS "${CMAKE_CURRENT_BINARY_DIR}/${_protoname}.pb.cc")
        set(${_protoname}_PROTO_HDRS "${CMAKE_CURRENT_BINARY_DIR}/${_protoname}.pb.h")
        set(${_protoname}_GRPC_SRCS "${CMAKE_CURRENT_BINARY_DIR}/${_protoname}.grpc.pb.cc")
        set(${_protoname}_GRPC_HDRS "${CMAKE_CURRENT_BINARY_DIR}/${_protoname}.grpc.pb.h")

        add_custom_command(
                OUTPUT "${${_protoname}_PROTO_SRCS}" "${${_protoname}_PROTO_HDRS}" "${${_protoname}_GRPC_SRCS}" "${${_protoname}_GRPC_HDRS}"
                COMMAND ${_PROTOBUF_PROTOC}
                ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}" --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
                -I "${${_protoname}_PROTOFILE_DIR}"
                --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXE}"
                "${${_protoname}_PROTOFILE}"
                DEPENDS "${${_protoname}_PROTOFILE}")
        list(APPEND _PROTO_SRCS ${${_protoname}_PROTO_SRCS})
        list(APPEND _PROTO_HDRS ${${_protoname}_PROTO_HDRS})
        list(APPEND _GRPC_SRCS ${${_protoname}_GRPC_SRCS})
        list(APPEND _GRPC_HDRS ${${_protoname}_GRPC_HDRS})
    endforeach ()
    set(${PROTO_SRCS} ${_PROTO_SRCS} PARENT_SCOPE)
    set(${PROTO_HDRS} ${_PROTO_HDRS} PARENT_SCOPE)
    set(${GRPC_SRCS} ${_GRPC_SRCS} PARENT_SCOPE)
    set(${GRPC_HDRS} ${_GRPC_HDRS} PARENT_SCOPE)
endfunction()