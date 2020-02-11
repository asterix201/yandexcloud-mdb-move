# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/service_account_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.iam.v1 import service_account_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_service__account__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iam/v1/service_account_service.proto',
  package='yandex.cloud.iam.v1',
  syntax='proto3',
  serialized_options=_b('\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'),
  serialized_pb=_b('\n1yandex/cloud/iam/v1/service_account_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a)yandex/cloud/iam/v1/service_account.proto\x1a yandex/cloud/access/access.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"D\n\x18GetServiceAccountRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x97\x01\n\x1aListServiceAccountsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"u\n\x1bListServiceAccountsResponse\x12=\n\x10service_accounts\x18\x01 \x03(\x0b\x32#.yandex.cloud.iam.v1.ServiceAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x93\x01\n\x1b\x43reateServiceAccountRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x33\n\x04name\x18\x02 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\":\n\x1c\x43reateServiceAccountMetadata\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\"\xcd\x01\n\x1bUpdateServiceAccountRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x33\n\x04name\x18\x03 \x01(\tB%\xe8\xc7\x31\x01\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\":\n\x1cUpdateServiceAccountMetadata\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\"G\n\x1b\x44\x65leteServiceAccountRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\":\n\x1c\x44\x65leteServiceAccountMetadata\x12\x1a\n\x12service_account_id\x18\x01 \x01(\t\"\x8d\x01\n#ListServiceAccountOperationsRequest\x12(\n\x12service_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"v\n$ListServiceAccountOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe8\r\n\x15ServiceAccountService\x12\x8f\x01\n\x03Get\x12-.yandex.cloud.iam.v1.GetServiceAccountRequest\x1a#.yandex.cloud.iam.v1.ServiceAccount\"4\x82\xd3\xe4\x93\x02.\x12,/iam/v1/serviceAccounts/{service_account_id}\x12\x8a\x01\n\x04List\x12/.yandex.cloud.iam.v1.ListServiceAccountsRequest\x1a\x30.yandex.cloud.iam.v1.ListServiceAccountsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/iam/v1/serviceAccounts\x12\xb3\x01\n\x06\x43reate\x12\x30.yandex.cloud.iam.v1.CreateServiceAccountRequest\x1a!.yandex.cloud.operation.Operation\"T\x82\xd3\xe4\x93\x02\x1c\"\x17/iam/v1/serviceAccounts:\x01*\xb2\xd2*.\n\x1c\x43reateServiceAccountMetadata\x12\x0eServiceAccount\x12\xc8\x01\n\x06Update\x12\x30.yandex.cloud.iam.v1.UpdateServiceAccountRequest\x1a!.yandex.cloud.operation.Operation\"i\x82\xd3\xe4\x93\x02\x31\x32,/iam/v1/serviceAccounts/{service_account_id}:\x01*\xb2\xd2*.\n\x1cUpdateServiceAccountMetadata\x12\x0eServiceAccount\x12\xcc\x01\n\x06\x44\x65lete\x12\x30.yandex.cloud.iam.v1.DeleteServiceAccountRequest\x1a!.yandex.cloud.operation.Operation\"m\x82\xd3\xe4\x93\x02.*,/iam/v1/serviceAccounts/{service_account_id}\xb2\xd2*5\n\x1c\x44\x65leteServiceAccountMetadata\x12\x15google.protobuf.Empty\x12\xb7\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/iam/v1/serviceAccounts/{resource_id}:listAccessBindings\x12\xe6\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x7f\x82\xd3\xe4\x93\x02<\"7/iam/v1/serviceAccounts/{resource_id}:setAccessBindings:\x01*\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x12\xf3\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x85\x01\x82\xd3\xe4\x93\x02?\":/iam/v1/serviceAccounts/{resource_id}:updateAccessBindings:\x01*\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x12\xc6\x01\n\x0eListOperations\x12\x38.yandex.cloud.iam.v1.ListServiceAccountOperationsRequest\x1a\x39.yandex.cloud.iam.v1.ListServiceAccountOperationsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/iam/v1/serviceAccounts/{service_account_id}/operationsBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_iam_dot_v1_dot_service__account__pb2.DESCRIPTOR,yandex_dot_cloud_dot_access_dot_access__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETSERVICEACCOUNTREQUEST = _descriptor.Descriptor(
  name='GetServiceAccountRequest',
  full_name='yandex.cloud.iam.v1.GetServiceAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.GetServiceAccountRequest.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
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
  serialized_start=320,
  serialized_end=388,
)


_LISTSERVICEACCOUNTSREQUEST = _descriptor.Descriptor(
  name='ListServiceAccountsRequest',
  full_name='yandex.cloud.iam.v1.ListServiceAccountsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.iam.v1.ListServiceAccountsRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.iam.v1.ListServiceAccountsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.iam.v1.ListServiceAccountsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.iam.v1.ListServiceAccountsRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\006<=1000'), file=DESCRIPTOR),
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
  serialized_start=391,
  serialized_end=542,
)


_LISTSERVICEACCOUNTSRESPONSE = _descriptor.Descriptor(
  name='ListServiceAccountsResponse',
  full_name='yandex.cloud.iam.v1.ListServiceAccountsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_accounts', full_name='yandex.cloud.iam.v1.ListServiceAccountsResponse.service_accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.iam.v1.ListServiceAccountsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=544,
  serialized_end=661,
)


_CREATESERVICEACCOUNTREQUEST = _descriptor.Descriptor(
  name='CreateServiceAccountRequest',
  full_name='yandex.cloud.iam.v1.CreateServiceAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.iam.v1.CreateServiceAccountRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.iam.v1.CreateServiceAccountRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iam.v1.CreateServiceAccountRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=256'), file=DESCRIPTOR),
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
  serialized_start=664,
  serialized_end=811,
)


_CREATESERVICEACCOUNTMETADATA = _descriptor.Descriptor(
  name='CreateServiceAccountMetadata',
  full_name='yandex.cloud.iam.v1.CreateServiceAccountMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.CreateServiceAccountMetadata.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=813,
  serialized_end=871,
)


_UPDATESERVICEACCOUNTREQUEST = _descriptor.Descriptor(
  name='UpdateServiceAccountRequest',
  full_name='yandex.cloud.iam.v1.UpdateServiceAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.UpdateServiceAccountRequest.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.iam.v1.UpdateServiceAccountRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.iam.v1.UpdateServiceAccountRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.iam.v1.UpdateServiceAccountRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=256'), file=DESCRIPTOR),
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
  serialized_start=874,
  serialized_end=1079,
)


_UPDATESERVICEACCOUNTMETADATA = _descriptor.Descriptor(
  name='UpdateServiceAccountMetadata',
  full_name='yandex.cloud.iam.v1.UpdateServiceAccountMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.UpdateServiceAccountMetadata.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1081,
  serialized_end=1139,
)


_DELETESERVICEACCOUNTREQUEST = _descriptor.Descriptor(
  name='DeleteServiceAccountRequest',
  full_name='yandex.cloud.iam.v1.DeleteServiceAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.DeleteServiceAccountRequest.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
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
  serialized_start=1141,
  serialized_end=1212,
)


_DELETESERVICEACCOUNTMETADATA = _descriptor.Descriptor(
  name='DeleteServiceAccountMetadata',
  full_name='yandex.cloud.iam.v1.DeleteServiceAccountMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.DeleteServiceAccountMetadata.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1214,
  serialized_end=1272,
)


_LISTSERVICEACCOUNTOPERATIONSREQUEST = _descriptor.Descriptor(
  name='ListServiceAccountOperationsRequest',
  full_name='yandex.cloud.iam.v1.ListServiceAccountOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.iam.v1.ListServiceAccountOperationsRequest.service_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.iam.v1.ListServiceAccountOperationsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.iam.v1.ListServiceAccountOperationsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
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
  serialized_start=1275,
  serialized_end=1416,
)


_LISTSERVICEACCOUNTOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='ListServiceAccountOperationsResponse',
  full_name='yandex.cloud.iam.v1.ListServiceAccountOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='yandex.cloud.iam.v1.ListServiceAccountOperationsResponse.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.iam.v1.ListServiceAccountOperationsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1418,
  serialized_end=1536,
)

_LISTSERVICEACCOUNTSRESPONSE.fields_by_name['service_accounts'].message_type = yandex_dot_cloud_dot_iam_dot_v1_dot_service__account__pb2._SERVICEACCOUNT
_UPDATESERVICEACCOUNTREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTSERVICEACCOUNTOPERATIONSRESPONSE.fields_by_name['operations'].message_type = yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['GetServiceAccountRequest'] = _GETSERVICEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['ListServiceAccountsRequest'] = _LISTSERVICEACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['ListServiceAccountsResponse'] = _LISTSERVICEACCOUNTSRESPONSE
DESCRIPTOR.message_types_by_name['CreateServiceAccountRequest'] = _CREATESERVICEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['CreateServiceAccountMetadata'] = _CREATESERVICEACCOUNTMETADATA
DESCRIPTOR.message_types_by_name['UpdateServiceAccountRequest'] = _UPDATESERVICEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['UpdateServiceAccountMetadata'] = _UPDATESERVICEACCOUNTMETADATA
DESCRIPTOR.message_types_by_name['DeleteServiceAccountRequest'] = _DELETESERVICEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['DeleteServiceAccountMetadata'] = _DELETESERVICEACCOUNTMETADATA
DESCRIPTOR.message_types_by_name['ListServiceAccountOperationsRequest'] = _LISTSERVICEACCOUNTOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListServiceAccountOperationsResponse'] = _LISTSERVICEACCOUNTOPERATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetServiceAccountRequest = _reflection.GeneratedProtocolMessageType('GetServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICEACCOUNTREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.GetServiceAccountRequest)
  })
_sym_db.RegisterMessage(GetServiceAccountRequest)

ListServiceAccountsRequest = _reflection.GeneratedProtocolMessageType('ListServiceAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVICEACCOUNTSREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListServiceAccountsRequest)
  })
_sym_db.RegisterMessage(ListServiceAccountsRequest)

ListServiceAccountsResponse = _reflection.GeneratedProtocolMessageType('ListServiceAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVICEACCOUNTSRESPONSE,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListServiceAccountsResponse)
  })
_sym_db.RegisterMessage(ListServiceAccountsResponse)

CreateServiceAccountRequest = _reflection.GeneratedProtocolMessageType('CreateServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVICEACCOUNTREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.CreateServiceAccountRequest)
  })
_sym_db.RegisterMessage(CreateServiceAccountRequest)

CreateServiceAccountMetadata = _reflection.GeneratedProtocolMessageType('CreateServiceAccountMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVICEACCOUNTMETADATA,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.CreateServiceAccountMetadata)
  })
_sym_db.RegisterMessage(CreateServiceAccountMetadata)

UpdateServiceAccountRequest = _reflection.GeneratedProtocolMessageType('UpdateServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVICEACCOUNTREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.UpdateServiceAccountRequest)
  })
_sym_db.RegisterMessage(UpdateServiceAccountRequest)

UpdateServiceAccountMetadata = _reflection.GeneratedProtocolMessageType('UpdateServiceAccountMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVICEACCOUNTMETADATA,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.UpdateServiceAccountMetadata)
  })
_sym_db.RegisterMessage(UpdateServiceAccountMetadata)

DeleteServiceAccountRequest = _reflection.GeneratedProtocolMessageType('DeleteServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVICEACCOUNTREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.DeleteServiceAccountRequest)
  })
_sym_db.RegisterMessage(DeleteServiceAccountRequest)

DeleteServiceAccountMetadata = _reflection.GeneratedProtocolMessageType('DeleteServiceAccountMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVICEACCOUNTMETADATA,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.DeleteServiceAccountMetadata)
  })
_sym_db.RegisterMessage(DeleteServiceAccountMetadata)

ListServiceAccountOperationsRequest = _reflection.GeneratedProtocolMessageType('ListServiceAccountOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVICEACCOUNTOPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListServiceAccountOperationsRequest)
  })
_sym_db.RegisterMessage(ListServiceAccountOperationsRequest)

ListServiceAccountOperationsResponse = _reflection.GeneratedProtocolMessageType('ListServiceAccountOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVICEACCOUNTOPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.iam.v1.service_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListServiceAccountOperationsResponse)
  })
_sym_db.RegisterMessage(ListServiceAccountOperationsResponse)


DESCRIPTOR._options = None
_GETSERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._options = None
_LISTSERVICEACCOUNTSREQUEST.fields_by_name['folder_id']._options = None
_LISTSERVICEACCOUNTSREQUEST.fields_by_name['page_size']._options = None
_LISTSERVICEACCOUNTSREQUEST.fields_by_name['page_token']._options = None
_LISTSERVICEACCOUNTSREQUEST.fields_by_name['filter']._options = None
_CREATESERVICEACCOUNTREQUEST.fields_by_name['folder_id']._options = None
_CREATESERVICEACCOUNTREQUEST.fields_by_name['name']._options = None
_CREATESERVICEACCOUNTREQUEST.fields_by_name['description']._options = None
_UPDATESERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._options = None
_UPDATESERVICEACCOUNTREQUEST.fields_by_name['name']._options = None
_UPDATESERVICEACCOUNTREQUEST.fields_by_name['description']._options = None
_DELETESERVICEACCOUNTREQUEST.fields_by_name['service_account_id']._options = None
_LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['service_account_id']._options = None
_LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['page_size']._options = None
_LISTSERVICEACCOUNTOPERATIONSREQUEST.fields_by_name['page_token']._options = None

_SERVICEACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='ServiceAccountService',
  full_name='yandex.cloud.iam.v1.ServiceAccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1539,
  serialized_end=3307,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.Get',
    index=0,
    containing_service=None,
    input_type=_GETSERVICEACCOUNTREQUEST,
    output_type=yandex_dot_cloud_dot_iam_dot_v1_dot_service__account__pb2._SERVICEACCOUNT,
    serialized_options=_b('\202\323\344\223\002.\022,/iam/v1/serviceAccounts/{service_account_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.List',
    index=1,
    containing_service=None,
    input_type=_LISTSERVICEACCOUNTSREQUEST,
    output_type=_LISTSERVICEACCOUNTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\031\022\027/iam/v1/serviceAccounts'),
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATESERVICEACCOUNTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002\034\"\027/iam/v1/serviceAccounts:\001*\262\322*.\n\034CreateServiceAccountMetadata\022\016ServiceAccount'),
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATESERVICEACCOUNTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\00212,/iam/v1/serviceAccounts/{service_account_id}:\001*\262\322*.\n\034UpdateServiceAccountMetadata\022\016ServiceAccount'),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETESERVICEACCOUNTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002.*,/iam/v1/serviceAccounts/{service_account_id}\262\322*5\n\034DeleteServiceAccountMetadata\022\025google.protobuf.Empty'),
  ),
  _descriptor.MethodDescriptor(
    name='ListAccessBindings',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.ListAccessBindings',
    index=5,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSRESPONSE,
    serialized_options=_b('\202\323\344\223\002:\0228/iam/v1/serviceAccounts/{resource_id}:listAccessBindings'),
  ),
  _descriptor.MethodDescriptor(
    name='SetAccessBindings',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.SetAccessBindings',
    index=6,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._SETACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002<\"7/iam/v1/serviceAccounts/{resource_id}:setAccessBindings:\001*\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAccessBindings',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.UpdateAccessBindings',
    index=7,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._UPDATEACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\002?\":/iam/v1/serviceAccounts/{resource_id}:updateAccessBindings:\001*\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty'),
  ),
  _descriptor.MethodDescriptor(
    name='ListOperations',
    full_name='yandex.cloud.iam.v1.ServiceAccountService.ListOperations',
    index=8,
    containing_service=None,
    input_type=_LISTSERVICEACCOUNTOPERATIONSREQUEST,
    output_type=_LISTSERVICEACCOUNTOPERATIONSRESPONSE,
    serialized_options=_b('\202\323\344\223\0029\0227/iam/v1/serviceAccounts/{service_account_id}/operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEACCOUNTSERVICE)

DESCRIPTOR.services_by_name['ServiceAccountService'] = _SERVICEACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)