import json

with open('raw.arr','r') as f:
    raw = f.read()

def print_arr(arr):
    for idx,val in enumerate(arr):
        print(f"{idx+1}:", val)


wrapper = json.loads(raw)
print("request wrapper:")
print_arr(wrapper)

request = json.loads(wrapper[1])
print("\nrequest:")
print_arr(request)

print("\nsettings:")
print_arr(request[3])


print("\ninoutbound settings:")
print_arr(request[3][13])

print("\noutbound fields:")
print_arr(request[3][13][0])

import request_pb2 as proto_request
import enums_pb2 as proto_enums

a = proto_request.Request()
a.bounds.top_left.latitude = 85
a.bounds.top_left.longitude = 180
a.bounds.bottom_right.latitude = -85
a.bounds.bottom_right.longitude = -180
a.settings.three = 1
a.settings.flight_class = proto_enums.FlightClass.FLIGHT_CLASS_ECONOMY
a.settings.date_options.month = 4 # april
a.settings.date_options.trip_date = proto_enums.TripDate.TRIP_DATE_2_WEEKS
a.settings.passengers.adults = 4
a.settings.passengers.children = 3
a.settings.passengers.infants_in_seat = 2
a.settings.price_bounds.high = 7500
a.settings.bags.carry_on_bags = 5
a.settings.inout_bound_settings.outbound.airport.one.one.airport = 'JFK'
a.settings.inout_bound_settings.outbound.stops = proto_enums.Stops.STOPS_ONE_OR_LESS
a.settings.inout_bound_settings.outbound.date = '2022-06-02'
a.settings.inout_bound_settings.outbound.duration.max_flight_duration = 1260
a.settings.inout_bound_settings.inbound.stops = proto_enums.Stops.STOPS_ONE_OR_LESS
a.settings.inout_bound_settings.inbound.date = '2022-06-06'
a.settings.inout_bound_settings.inbound.duration.max_flight_duration = 1260
a.settings.flights_only = proto_enums.FlightOnly.FLIGHT_ONLY_YES
#print(a)

from protobuf2arr import serialize_msg2arr
from protobuf2arr.serializer import msg_to_arr

w = proto_request.RequestWrapper()
w.payload = serialize_msg2arr(a)
final = serialize_msg2arr(w)
print("\nfinal:")
print(final)
print("original:")
print(raw)