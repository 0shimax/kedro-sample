# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: onnxGrpcServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='onnxGrpcServer.proto',
  package='onnxGrpcServer',
  syntax='proto3',
  serialized_options=b'\n\007ex.grpc\242\002\003HSW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14onnxGrpcServer.proto\x12\x0eonnxGrpcServer\"|\n\tFloatData\x12\x0f\n\x07\x65ngines\x18\x01 \x01(\x02\x12\x1a\n\x12passenger_capacity\x18\x02 \x01(\x02\x12\x0c\n\x04\x63rew\x18\x03 \x01(\x02\x12\x16\n\x0e\x63ompany_rating\x18\x04 \x01(\x02\x12\x1c\n\x14review_scores_rating\x18\x05 \x01(\x02\"c\n\x0f\x43\x61tegoricalData\x12\x18\n\x10\x64_check_complete\x18\x01 \x01(\t\x12\x1f\n\x17moon_clearance_complete\x18\x02 \x01(\t\x12\x15\n\riata_approved\x18\x03 \x01(\t\"|\n\x08\x46\x65\x61tures\x12\x31\n\x0e\x66loat_features\x18\x01 \x01(\x0b\x32\x19.onnxGrpcServer.FloatData\x12=\n\x14\x63\x61tegorical_features\x18\x02 \x01(\x0b\x32\x1f.onnxGrpcServer.CategoricalData\"\x19\n\tPredicted\x12\x0c\n\x04prob\x18\x01 \x01(\x02\"\x1d\n\x0cUpdateParams\x12\r\n\x05param\x18\x01 \x01(\t\"\x17\n\x05Reply\x12\x0e\n\x06status\x18\x01 \x01(\t2\xa4\x01\n\x15\x43TCVInferenceServicer\x12\x44\n\x07predict\x12\x18.onnxGrpcServer.Features\x1a\x19.onnxGrpcServer.Predicted\"\x00(\x01\x30\x01\x12\x45\n\x0cupdate_model\x12\x1c.onnxGrpcServer.UpdateParams\x1a\x15.onnxGrpcServer.Reply\"\x00\x42\x0f\n\x07\x65x.grpc\xa2\x02\x03HSWb\x06proto3'
)




_FLOATDATA = _descriptor.Descriptor(
  name='FloatData',
  full_name='onnxGrpcServer.FloatData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='engines', full_name='onnxGrpcServer.FloatData.engines', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passenger_capacity', full_name='onnxGrpcServer.FloatData.passenger_capacity', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='crew', full_name='onnxGrpcServer.FloatData.crew', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_rating', full_name='onnxGrpcServer.FloatData.company_rating', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='review_scores_rating', full_name='onnxGrpcServer.FloatData.review_scores_rating', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=164,
)


_CATEGORICALDATA = _descriptor.Descriptor(
  name='CategoricalData',
  full_name='onnxGrpcServer.CategoricalData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='d_check_complete', full_name='onnxGrpcServer.CategoricalData.d_check_complete', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='moon_clearance_complete', full_name='onnxGrpcServer.CategoricalData.moon_clearance_complete', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iata_approved', full_name='onnxGrpcServer.CategoricalData.iata_approved', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=265,
)


_FEATURES = _descriptor.Descriptor(
  name='Features',
  full_name='onnxGrpcServer.Features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='float_features', full_name='onnxGrpcServer.Features.float_features', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='categorical_features', full_name='onnxGrpcServer.Features.categorical_features', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=391,
)


_PREDICTED = _descriptor.Descriptor(
  name='Predicted',
  full_name='onnxGrpcServer.Predicted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prob', full_name='onnxGrpcServer.Predicted.prob', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=418,
)


_UPDATEPARAMS = _descriptor.Descriptor(
  name='UpdateParams',
  full_name='onnxGrpcServer.UpdateParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='param', full_name='onnxGrpcServer.UpdateParams.param', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=449,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='onnxGrpcServer.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='onnxGrpcServer.Reply.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=474,
)

_FEATURES.fields_by_name['float_features'].message_type = _FLOATDATA
_FEATURES.fields_by_name['categorical_features'].message_type = _CATEGORICALDATA
DESCRIPTOR.message_types_by_name['FloatData'] = _FLOATDATA
DESCRIPTOR.message_types_by_name['CategoricalData'] = _CATEGORICALDATA
DESCRIPTOR.message_types_by_name['Features'] = _FEATURES
DESCRIPTOR.message_types_by_name['Predicted'] = _PREDICTED
DESCRIPTOR.message_types_by_name['UpdateParams'] = _UPDATEPARAMS
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FloatData = _reflection.GeneratedProtocolMessageType('FloatData', (_message.Message,), {
  'DESCRIPTOR' : _FLOATDATA,
  '__module__' : 'onnxGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:onnxGrpcServer.FloatData)
  })
_sym_db.RegisterMessage(FloatData)

CategoricalData = _reflection.GeneratedProtocolMessageType('CategoricalData', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORICALDATA,
  '__module__' : 'onnxGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:onnxGrpcServer.CategoricalData)
  })
_sym_db.RegisterMessage(CategoricalData)

Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {
  'DESCRIPTOR' : _FEATURES,
  '__module__' : 'onnxGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:onnxGrpcServer.Features)
  })
_sym_db.RegisterMessage(Features)

Predicted = _reflection.GeneratedProtocolMessageType('Predicted', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTED,
  '__module__' : 'onnxGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:onnxGrpcServer.Predicted)
  })
_sym_db.RegisterMessage(Predicted)

UpdateParams = _reflection.GeneratedProtocolMessageType('UpdateParams', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPARAMS,
  '__module__' : 'onnxGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:onnxGrpcServer.UpdateParams)
  })
_sym_db.RegisterMessage(UpdateParams)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'onnxGrpcServer_pb2'
  # @@protoc_insertion_point(class_scope:onnxGrpcServer.Reply)
  })
_sym_db.RegisterMessage(Reply)


DESCRIPTOR._options = None

_CTCVINFERENCESERVICER = _descriptor.ServiceDescriptor(
  name='CTCVInferenceServicer',
  full_name='onnxGrpcServer.CTCVInferenceServicer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=477,
  serialized_end=641,
  methods=[
  _descriptor.MethodDescriptor(
    name='predict',
    full_name='onnxGrpcServer.CTCVInferenceServicer.predict',
    index=0,
    containing_service=None,
    input_type=_FEATURES,
    output_type=_PREDICTED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update_model',
    full_name='onnxGrpcServer.CTCVInferenceServicer.update_model',
    index=1,
    containing_service=None,
    input_type=_UPDATEPARAMS,
    output_type=_REPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CTCVINFERENCESERVICER)

DESCRIPTOR.services_by_name['CTCVInferenceServicer'] = _CTCVINFERENCESERVICER

# @@protoc_insertion_point(module_scope)