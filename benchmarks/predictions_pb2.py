# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: predictions.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11predictions.proto\"&\n\x11PredictionRequest\x12\x11\n\tid_client\x18\x01 \x01(\t\"/\n\nPrediction\x12\x12\n\nclass_name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"6\n\x12PredictionResponse\x12 \n\x0bpredictions\x18\x01 \x03(\x0b\x32\x0b.Prediction2H\n\x0bPredictions\x12\x39\n\x0eGetPredictions\x12\x12.PredictionRequest\x1a\x13.PredictionResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'predictions_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PREDICTIONREQUEST._serialized_start=21
  _PREDICTIONREQUEST._serialized_end=59
  _PREDICTION._serialized_start=61
  _PREDICTION._serialized_end=108
  _PREDICTIONRESPONSE._serialized_start=110
  _PREDICTIONRESPONSE._serialized_end=164
  _PREDICTIONS._serialized_start=166
  _PREDICTIONS._serialized_end=238
# @@protoc_insertion_point(module_scope)
