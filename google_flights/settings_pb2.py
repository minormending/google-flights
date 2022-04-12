# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: settings.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nullable_pb2 as nullable__pb2
import enums_pb2 as enums__pb2
import inoutbound_pb2 as inoutbound__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0esettings.proto\x12\x0egoogle_flights\x1a\x0enullable.proto\x1a\x0b\x65nums.proto\x1a\x10inoutbound.proto\"\x90\x03\n\x08Settings\x12\r\n\x05three\x18\x03 \x01(\x05\x12\x31\n\x0c\x64\x61te_options\x18\x05 \x01(\x0b\x32\x1b.google_flights.DateOptions\x12\x31\n\x0c\x66light_class\x18\x06 \x01(\x0e\x32\x1b.google_flights.FlightClass\x12.\n\npassengers\x18\x07 \x01(\x0b\x32\x1a.google_flights.Passengers\x12\x36\n\x0cprice_bounds\x18\x08 \x01(\x0b\x32\x1b.google_flights.PriceBoundsH\x00\x88\x01\x01\x12\"\n\x04\x62\x61gs\x18\x0b \x01(\x0b\x32\x14.google_flights.Bags\x12@\n\x14inout_bound_settings\x18\x0e \x01(\x0b\x32\".google_flights.InOutBoundSettings\x12\x30\n\x0c\x66lights_only\x18\x1a \x01(\x0e\x32\x1a.google_flights.FlightOnlyB\x0f\n\r_price_bounds\"I\n\x0b\x44\x61teOptions\x12\r\n\x05month\x18\x01 \x01(\x05\x12+\n\ttrip_date\x18\x02 \x01(\x0e\x32\x18.google_flights.TripDate\"_\n\nPassengers\x12\x0e\n\x06\x61\x64ults\x18\x01 \x01(\x05\x12\x10\n\x08\x63hildren\x18\x02 \x01(\x05\x12\x16\n\x0einfants_on_lap\x18\x03 \x01(\x05\x12\x17\n\x0finfants_in_seat\x18\x04 \x01(\x05\"/\n\x0bPriceBounds\x12\x12\n\x03low\x18\x01 \x01(\x05\x42\x05\xda\xb6\x18\x01\x30\x12\x0c\n\x04high\x18\x02 \x01(\x05\"*\n\x04\x42\x61gs\x12\x15\n\rcarry_on_bags\x18\x01 \x01(\x05\x12\x0b\n\x03two\x18\x02 \x01(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'settings_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRICEBOUNDS.fields_by_name['low']._options = None
  _PRICEBOUNDS.fields_by_name['low']._serialized_options = b'\332\266\030\0010'
  _SETTINGS._serialized_start=82
  _SETTINGS._serialized_end=482
  _DATEOPTIONS._serialized_start=484
  _DATEOPTIONS._serialized_end=557
  _PASSENGERS._serialized_start=559
  _PASSENGERS._serialized_end=654
  _PRICEBOUNDS._serialized_start=656
  _PRICEBOUNDS._serialized_end=703
  _BAGS._serialized_start=705
  _BAGS._serialized_end=747
# @@protoc_insertion_point(module_scope)
