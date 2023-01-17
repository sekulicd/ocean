# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ocean/v1/account.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ocean.v1 import types_pb2 as ocean_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16ocean/v1/account.proto\x12\x08ocean.v1\x1a\x14ocean/v1/types.proto\"R\n\x19\x43reateAccountBIP44Request\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12\x1f\n\x0b\x65xtra_xpubs\x18\x02 \x03(\tR\nextraXpubs\"V\n\x1a\x43reateAccountBIP44Response\x12\x38\n\x0c\x61\x63\x63ount_info\x18\x01 \x01(\x0b\x32\x15.ocean.v1.AccountInfoR\x0b\x61\x63\x63ountInfo\"4\n\x1c\x43reateAccountMultiSigRequest\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\"Y\n\x1d\x43reateAccountMultiSigResponse\x12\x38\n\x0c\x61\x63\x63ount_info\x18\x01 \x01(\x0b\x32\x15.ocean.v1.AccountInfoR\x0b\x61\x63\x63ountInfo\"2\n\x1a\x43reateAccountCustomRequest\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\"W\n\x1b\x43reateAccountCustomResponse\x12\x38\n\x0c\x61\x63\x63ount_info\x18\x01 \x01(\x0b\x32\x15.ocean.v1.AccountInfoR\x0b\x61\x63\x63ountInfo\"n\n\x19SetAccountTemplateRequest\x12!\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\tR\x0b\x61\x63\x63ountName\x12.\n\x08template\x18\x02 \x01(\x0b\x32\x12.ocean.v1.TemplateR\x08template\"\x1c\n\x1aSetAccountTemplateResponse\"V\n\x16\x44\x65riveAddressesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12(\n\x10num_of_addresses\x18\x02 \x01(\x04R\x0enumOfAddresses\"7\n\x17\x44\x65riveAddressesResponse\x12\x1c\n\taddresses\x18\x01 \x03(\tR\taddresses\"\\\n\x1c\x44\x65riveChangeAddressesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12(\n\x10num_of_addresses\x18\x02 \x01(\x04R\x0enumOfAddresses\"=\n\x1d\x44\x65riveChangeAddressesResponse\x12\x1c\n\taddresses\x18\x01 \x03(\tR\taddresses\"*\n\x14ListAddressesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"5\n\x15ListAddressesResponse\x12\x1c\n\taddresses\x18\x01 \x03(\tR\taddresses\"B\n\x0e\x42\x61lanceRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\taddresses\x18\x03 \x03(\tR\taddresses\"\xa6\x01\n\x0f\x42\x61lanceResponse\x12@\n\x07\x62\x61lance\x18\x01 \x03(\x0b\x32&.ocean.v1.BalanceResponse.BalanceEntryR\x07\x62\x61lance\x1aQ\n\x0c\x42\x61lanceEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x15.ocean.v1.BalanceInfoR\x05value:\x02\x38\x01\"D\n\x10ListUtxosRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\taddresses\x18\x03 \x03(\tR\taddresses\"\x81\x01\n\x11ListUtxosResponse\x12\x38\n\x0fspendable_utxos\x18\x01 \x01(\x0b\x32\x0f.ocean.v1.UtxosR\x0espendableUtxos\x12\x32\n\x0clocked_utxos\x18\x02 \x01(\x0b\x32\x0f.ocean.v1.UtxosR\x0blockedUtxos\"*\n\x14\x44\x65leteAccountRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\x17\n\x15\x44\x65leteAccountResponse\"B\n\x16SetAccountLabelRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05label\x18\x02 \x01(\tR\x05label\"\x19\n\x17SetAccountLabelResponse2\xe4\x07\n\x0e\x41\x63\x63ountService\x12_\n\x12\x43reateAccountBIP44\x12#.ocean.v1.CreateAccountBIP44Request\x1a$.ocean.v1.CreateAccountBIP44Response\x12h\n\x15\x43reateAccountMultiSig\x12&.ocean.v1.CreateAccountMultiSigRequest\x1a\'.ocean.v1.CreateAccountMultiSigResponse\x12\x62\n\x13\x43reateAccountCustom\x12$.ocean.v1.CreateAccountCustomRequest\x1a%.ocean.v1.CreateAccountCustomResponse\x12_\n\x12SetAccountTemplate\x12#.ocean.v1.SetAccountTemplateRequest\x1a$.ocean.v1.SetAccountTemplateResponse\x12V\n\x0f\x44\x65riveAddresses\x12 .ocean.v1.DeriveAddressesRequest\x1a!.ocean.v1.DeriveAddressesResponse\x12h\n\x15\x44\x65riveChangeAddresses\x12&.ocean.v1.DeriveChangeAddressesRequest\x1a\'.ocean.v1.DeriveChangeAddressesResponse\x12P\n\rListAddresses\x12\x1e.ocean.v1.ListAddressesRequest\x1a\x1f.ocean.v1.ListAddressesResponse\x12>\n\x07\x42\x61lance\x12\x18.ocean.v1.BalanceRequest\x1a\x19.ocean.v1.BalanceResponse\x12\x44\n\tListUtxos\x12\x1a.ocean.v1.ListUtxosRequest\x1a\x1b.ocean.v1.ListUtxosResponse\x12P\n\rDeleteAccount\x12\x1e.ocean.v1.DeleteAccountRequest\x1a\x1f.ocean.v1.DeleteAccountResponse\x12V\n\x0fSetAccountLabel\x12 .ocean.v1.SetAccountLabelRequest\x1a!.ocean.v1.SetAccountLabelResponseB\xa5\x01\n\x0c\x63om.ocean.v1B\x0c\x41\x63\x63ountProtoP\x01ZFgithub.com/vulpemventures/ocean/api-spec/protobuf/gen/ocean/v1;oceanv1\xa2\x02\x03OXX\xaa\x02\x08Ocean.V1\xca\x02\x08Ocean\\V1\xe2\x02\x14Ocean\\V1\\GPBMetadata\xea\x02\tOcean::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ocean.v1.account_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\014com.ocean.v1B\014AccountProtoP\001ZFgithub.com/vulpemventures/ocean/api-spec/protobuf/gen/ocean/v1;oceanv1\242\002\003OXX\252\002\010Ocean.V1\312\002\010Ocean\\V1\342\002\024Ocean\\V1\\GPBMetadata\352\002\tOcean::V1'
  _BALANCERESPONSE_BALANCEENTRY._options = None
  _BALANCERESPONSE_BALANCEENTRY._serialized_options = b'8\001'
  _CREATEACCOUNTBIP44REQUEST._serialized_start=58
  _CREATEACCOUNTBIP44REQUEST._serialized_end=140
  _CREATEACCOUNTBIP44RESPONSE._serialized_start=142
  _CREATEACCOUNTBIP44RESPONSE._serialized_end=228
  _CREATEACCOUNTMULTISIGREQUEST._serialized_start=230
  _CREATEACCOUNTMULTISIGREQUEST._serialized_end=282
  _CREATEACCOUNTMULTISIGRESPONSE._serialized_start=284
  _CREATEACCOUNTMULTISIGRESPONSE._serialized_end=373
  _CREATEACCOUNTCUSTOMREQUEST._serialized_start=375
  _CREATEACCOUNTCUSTOMREQUEST._serialized_end=425
  _CREATEACCOUNTCUSTOMRESPONSE._serialized_start=427
  _CREATEACCOUNTCUSTOMRESPONSE._serialized_end=514
  _SETACCOUNTTEMPLATEREQUEST._serialized_start=516
  _SETACCOUNTTEMPLATEREQUEST._serialized_end=626
  _SETACCOUNTTEMPLATERESPONSE._serialized_start=628
  _SETACCOUNTTEMPLATERESPONSE._serialized_end=656
  _DERIVEADDRESSESREQUEST._serialized_start=658
  _DERIVEADDRESSESREQUEST._serialized_end=744
  _DERIVEADDRESSESRESPONSE._serialized_start=746
  _DERIVEADDRESSESRESPONSE._serialized_end=801
  _DERIVECHANGEADDRESSESREQUEST._serialized_start=803
  _DERIVECHANGEADDRESSESREQUEST._serialized_end=895
  _DERIVECHANGEADDRESSESRESPONSE._serialized_start=897
  _DERIVECHANGEADDRESSESRESPONSE._serialized_end=958
  _LISTADDRESSESREQUEST._serialized_start=960
  _LISTADDRESSESREQUEST._serialized_end=1002
  _LISTADDRESSESRESPONSE._serialized_start=1004
  _LISTADDRESSESRESPONSE._serialized_end=1057
  _BALANCEREQUEST._serialized_start=1059
  _BALANCEREQUEST._serialized_end=1125
  _BALANCERESPONSE._serialized_start=1128
  _BALANCERESPONSE._serialized_end=1294
  _BALANCERESPONSE_BALANCEENTRY._serialized_start=1213
  _BALANCERESPONSE_BALANCEENTRY._serialized_end=1294
  _LISTUTXOSREQUEST._serialized_start=1296
  _LISTUTXOSREQUEST._serialized_end=1364
  _LISTUTXOSRESPONSE._serialized_start=1367
  _LISTUTXOSRESPONSE._serialized_end=1496
  _DELETEACCOUNTREQUEST._serialized_start=1498
  _DELETEACCOUNTREQUEST._serialized_end=1540
  _DELETEACCOUNTRESPONSE._serialized_start=1542
  _DELETEACCOUNTRESPONSE._serialized_end=1565
  _SETACCOUNTLABELREQUEST._serialized_start=1567
  _SETACCOUNTLABELREQUEST._serialized_end=1633
  _SETACCOUNTLABELRESPONSE._serialized_start=1635
  _SETACCOUNTLABELRESPONSE._serialized_end=1660
  _ACCOUNTSERVICE._serialized_start=1663
  _ACCOUNTSERVICE._serialized_end=2659
# @@protoc_insertion_point(module_scope)
