# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dianping.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64ianping.proto\x12\x04grpc\"#\n\x10RecommendRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\"\n\x0eRecommendReply\x12\x10\n\x08shop_ids\x18\x01 \x03(\x05\x32\x45\n\x08\x44ianPing\x12\x39\n\tRecommend\x12\x16.grpc.RecommendRequest\x1a\x14.grpc.RecommendReplyb\x06proto3')



_RECOMMENDREQUEST = DESCRIPTOR.message_types_by_name['RecommendRequest']
_RECOMMENDREPLY = DESCRIPTOR.message_types_by_name['RecommendReply']
RecommendRequest = _reflection.GeneratedProtocolMessageType('RecommendRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDREQUEST,
  '__module__' : 'dianping_pb2'
  # @@protoc_insertion_point(class_scope:grpc.RecommendRequest)
  })
_sym_db.RegisterMessage(RecommendRequest)

RecommendReply = _reflection.GeneratedProtocolMessageType('RecommendReply', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDREPLY,
  '__module__' : 'dianping_pb2'
  # @@protoc_insertion_point(class_scope:grpc.RecommendReply)
  })
_sym_db.RegisterMessage(RecommendReply)

_DIANPING = DESCRIPTOR.services_by_name['DianPing']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECOMMENDREQUEST._serialized_start=24
  _RECOMMENDREQUEST._serialized_end=59
  _RECOMMENDREPLY._serialized_start=61
  _RECOMMENDREPLY._serialized_end=95
  _DIANPING._serialized_start=97
  _DIANPING._serialized_end=166
# @@protoc_insertion_point(module_scope)