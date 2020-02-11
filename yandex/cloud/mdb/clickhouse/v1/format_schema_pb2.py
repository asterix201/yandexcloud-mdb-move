# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/format_schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/clickhouse/v1/format_schema.proto',
  package='yandex.cloud.mdb.clickhouse.v1',
  syntax='proto3',
  serialized_options=_b('\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse'),
  serialized_pb=_b('\n2yandex/cloud/mdb/clickhouse/v1/format_schema.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\"}\n\x0c\x46ormatSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12>\n\x04type\x18\x03 \x01(\x0e\x32\x30.yandex.cloud.mdb.clickhouse.v1.FormatSchemaType\x12\x0b\n\x03uri\x18\x04 \x01(\t*y\n\x10\x46ormatSchemaType\x12\"\n\x1e\x46ORMAT_SCHEMA_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x46ORMAT_SCHEMA_TYPE_PROTOBUF\x10\x01\x12 \n\x1c\x46ORMAT_SCHEMA_TYPE_CAPNPROTO\x10\x02\x42s\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3')
)

_FORMATSCHEMATYPE = _descriptor.EnumDescriptor(
  name='FormatSchemaType',
  full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchemaType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORMAT_SCHEMA_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMAT_SCHEMA_TYPE_PROTOBUF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMAT_SCHEMA_TYPE_CAPNPROTO', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=213,
  serialized_end=334,
)
_sym_db.RegisterEnumDescriptor(_FORMATSCHEMATYPE)

FormatSchemaType = enum_type_wrapper.EnumTypeWrapper(_FORMATSCHEMATYPE)
FORMAT_SCHEMA_TYPE_UNSPECIFIED = 0
FORMAT_SCHEMA_TYPE_PROTOBUF = 1
FORMAT_SCHEMA_TYPE_CAPNPROTO = 2



_FORMATSCHEMA = _descriptor.Descriptor(
  name='FormatSchema',
  full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchema.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchema.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchema.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchema.uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=86,
  serialized_end=211,
)

_FORMATSCHEMA.fields_by_name['type'].enum_type = _FORMATSCHEMATYPE
DESCRIPTOR.message_types_by_name['FormatSchema'] = _FORMATSCHEMA
DESCRIPTOR.enum_types_by_name['FormatSchemaType'] = _FORMATSCHEMATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FormatSchema = _reflection.GeneratedProtocolMessageType('FormatSchema', (_message.Message,), {
  'DESCRIPTOR' : _FORMATSCHEMA,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.FormatSchema)
  })
_sym_db.RegisterMessage(FormatSchema)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)