# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1/config/mysql5_7.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/mysql/v1/config/mysql5_7.proto',
  package='yandex.cloud.mdb.mysql.v1.config',
  syntax='proto3',
  serialized_options=_b('\n$yandex.cloud.api.mdb.mysql.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1/config;mysql'),
  serialized_pb=_b('\n/yandex/cloud/mdb/mysql/v1/config/mysql5_7.proto\x12 yandex.cloud.mdb.mysql.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\x9c\n\n\x0eMysqlConfig5_7\x12K\n\x17innodb_buffer_pool_size\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\r\xfa\xc7\x31\t>=5242880\x12\x42\n\x0fmax_connections\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-10000\x12\x35\n\x0flong_query_time\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12/\n\x0bgeneral_log\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\taudit_log\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12J\n\x08sql_mode\x18\x06 \x03(\x0e\x32\x38.yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.SQLMode\x12K\n\x12max_allowed_packet\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x12\xfa\xc7\x31\x0e\x31\x30\x32\x34-134217728\x12\x62\n\x1d\x64\x65\x66\x61ult_authentication_plugin\x18\x08 \x01(\x0e\x32;.yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.AuthPlugin\"\xea\x04\n\x07SQLMode\x12\x17\n\x13SQLMODE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x41LLOW_INVALID_DATES\x10\x01\x12\x0f\n\x0b\x41NSI_QUOTES\x10\x02\x12\x1e\n\x1a\x45RROR_FOR_DIVISION_BY_ZERO\x10\x03\x12\x17\n\x13HIGH_NOT_PRECEDENCE\x10\x04\x12\x10\n\x0cIGNORE_SPACE\x10\x05\x12\x19\n\x15NO_AUTO_VALUE_ON_ZERO\x10\x06\x12\x18\n\x14NO_BACKSLASH_ESCAPES\x10\x07\x12\x1a\n\x16NO_ENGINE_SUBSTITUTION\x10\x08\x12\x1b\n\x17NO_UNSIGNED_SUBTRACTION\x10\t\x12\x10\n\x0cNO_ZERO_DATE\x10\n\x12\x13\n\x0fNO_ZERO_IN_DATE\x10\x0b\x12\x14\n\x10NO_FIELD_OPTIONS\x10\x0c\x12\x12\n\x0eNO_KEY_OPTIONS\x10\r\x12\x14\n\x10NO_TABLE_OPTIONS\x10\x0e\x12\x16\n\x12ONLY_FULL_GROUP_BY\x10\x0f\x12\x1b\n\x17PAD_CHAR_TO_FULL_LENGTH\x10\x10\x12\x13\n\x0fPIPES_AS_CONCAT\x10\x11\x12\x11\n\rREAL_AS_FLOAT\x10\x12\x12\x15\n\x11STRICT_ALL_TABLES\x10\x13\x12\x17\n\x13STRICT_TRANS_TABLES\x10\x14\x12\x08\n\x04\x41NSI\x10\x15\x12\x0f\n\x0bTRADITIONAL\x10\x16\x12\x07\n\x03\x44\x42\x32\x10\x17\x12\t\n\x05MAXDB\x10\x18\x12\t\n\x05MSSQL\x10\x19\x12\x0c\n\x08MYSQL323\x10\x1a\x12\x0b\n\x07MYSQL40\x10\x1b\x12\n\n\x06ORACLE\x10\x1c\x12\x0e\n\nPOSTGRESQL\x10\x1d\"x\n\nAuthPlugin\x12\x1b\n\x17\x41UTH_PLUGIN_UNSPECIFIED\x10\x00\x12\x19\n\x15MYSQL_NATIVE_PASSWORD\x10\x01\x12\x1d\n\x15\x43\x41\x43HING_SHA2_PASSWORD\x10\x02\x1a\x02\x08\x01\x12\x13\n\x0fSHA256_PASSWORD\x10\x03\"\xf0\x01\n\x11MysqlConfigSet5_7\x12J\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x30.yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7\x12\x45\n\x0buser_config\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7\x12H\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x30.yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7Br\n$yandex.cloud.api.mdb.mysql.v1.configZJgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1/config;mysqlb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_MYSQLCONFIG5_7_SQLMODE = _descriptor.EnumDescriptor(
  name='SQLMode',
  full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.SQLMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SQLMODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLOW_INVALID_DATES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANSI_QUOTES', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FOR_DIVISION_BY_ZERO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH_NOT_PRECEDENCE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IGNORE_SPACE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_AUTO_VALUE_ON_ZERO', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_BACKSLASH_ESCAPES', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ENGINE_SUBSTITUTION', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_UNSIGNED_SUBTRACTION', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ZERO_DATE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ZERO_IN_DATE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_FIELD_OPTIONS', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_KEY_OPTIONS', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_TABLE_OPTIONS', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONLY_FULL_GROUP_BY', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAD_CHAR_TO_FULL_LENGTH', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIPES_AS_CONCAT', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REAL_AS_FLOAT', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRICT_ALL_TABLES', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRICT_TRANS_TABLES', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANSI', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADITIONAL', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DB2', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXDB', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSSQL', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MYSQL323', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MYSQL40', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORACLE', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTGRESQL', index=29, number=29,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=717,
  serialized_end=1335,
)
_sym_db.RegisterEnumDescriptor(_MYSQLCONFIG5_7_SQLMODE)

_MYSQLCONFIG5_7_AUTHPLUGIN = _descriptor.EnumDescriptor(
  name='AuthPlugin',
  full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.AuthPlugin',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTH_PLUGIN_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MYSQL_NATIVE_PASSWORD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CACHING_SHA2_PASSWORD', index=2, number=2,
      serialized_options=_b('\010\001'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHA256_PASSWORD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1337,
  serialized_end=1457,
)
_sym_db.RegisterEnumDescriptor(_MYSQLCONFIG5_7_AUTHPLUGIN)


_MYSQLCONFIG5_7 = _descriptor.Descriptor(
  name='MysqlConfig5_7',
  full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='innodb_buffer_pool_size', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.innodb_buffer_pool_size', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\t>=5242880'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_connections', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.max_connections', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\01010-10000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_query_time', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.long_query_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='general_log', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.general_log', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audit_log', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.audit_log', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sql_mode', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.sql_mode', index=5,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_allowed_packet', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.max_allowed_packet', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\0161024-134217728'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_authentication_plugin', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7.default_authentication_plugin', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MYSQLCONFIG5_7_SQLMODE,
    _MYSQLCONFIG5_7_AUTHPLUGIN,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=1457,
)


_MYSQLCONFIGSET5_7 = _descriptor.Descriptor(
  name='MysqlConfigSet5_7',
  full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfigSet5_7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='effective_config', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfigSet5_7.effective_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_config', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfigSet5_7.user_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_config', full_name='yandex.cloud.mdb.mysql.v1.config.MysqlConfigSet5_7.default_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1460,
  serialized_end=1700,
)

_MYSQLCONFIG5_7.fields_by_name['innodb_buffer_pool_size'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MYSQLCONFIG5_7.fields_by_name['max_connections'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MYSQLCONFIG5_7.fields_by_name['long_query_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_MYSQLCONFIG5_7.fields_by_name['general_log'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MYSQLCONFIG5_7.fields_by_name['audit_log'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_MYSQLCONFIG5_7.fields_by_name['sql_mode'].enum_type = _MYSQLCONFIG5_7_SQLMODE
_MYSQLCONFIG5_7.fields_by_name['max_allowed_packet'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MYSQLCONFIG5_7.fields_by_name['default_authentication_plugin'].enum_type = _MYSQLCONFIG5_7_AUTHPLUGIN
_MYSQLCONFIG5_7_SQLMODE.containing_type = _MYSQLCONFIG5_7
_MYSQLCONFIG5_7_AUTHPLUGIN.containing_type = _MYSQLCONFIG5_7
_MYSQLCONFIGSET5_7.fields_by_name['effective_config'].message_type = _MYSQLCONFIG5_7
_MYSQLCONFIGSET5_7.fields_by_name['user_config'].message_type = _MYSQLCONFIG5_7
_MYSQLCONFIGSET5_7.fields_by_name['default_config'].message_type = _MYSQLCONFIG5_7
DESCRIPTOR.message_types_by_name['MysqlConfig5_7'] = _MYSQLCONFIG5_7
DESCRIPTOR.message_types_by_name['MysqlConfigSet5_7'] = _MYSQLCONFIGSET5_7
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MysqlConfig5_7 = _reflection.GeneratedProtocolMessageType('MysqlConfig5_7', (_message.Message,), {
  'DESCRIPTOR' : _MYSQLCONFIG5_7,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.config.mysql5_7_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.config.MysqlConfig5_7)
  })
_sym_db.RegisterMessage(MysqlConfig5_7)

MysqlConfigSet5_7 = _reflection.GeneratedProtocolMessageType('MysqlConfigSet5_7', (_message.Message,), {
  'DESCRIPTOR' : _MYSQLCONFIGSET5_7,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.config.mysql5_7_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.config.MysqlConfigSet5_7)
  })
_sym_db.RegisterMessage(MysqlConfigSet5_7)


DESCRIPTOR._options = None
_MYSQLCONFIG5_7_AUTHPLUGIN.values_by_name["CACHING_SHA2_PASSWORD"]._options = None
_MYSQLCONFIG5_7.fields_by_name['innodb_buffer_pool_size']._options = None
_MYSQLCONFIG5_7.fields_by_name['max_connections']._options = None
_MYSQLCONFIG5_7.fields_by_name['max_allowed_packet']._options = None
# @@protoc_insertion_point(module_scope)
