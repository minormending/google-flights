import json

with open('raw.arr','r') as f:
    raw = f.read()

def print_arr(arr):
    for idx,val in enumerate(arr):
        print(f"{idx+1}:", val)


wrapper = json.loads(raw)
print("wrapper:")
print_arr(wrapper)

request = json.loads(wrapper[1])
print("\nrequest:")
print_arr(request)

print("\nsettings:")
print_arr(request[3])


print("\nsettings fields:")
print_arr(request[3][13])

print("\noutbound fields:")
print_arr(request[3][13][0])

import flights_pb2
a = flights_pb2.FlightEstimate()
a.bounds.top_left.latitude = 85
a.bounds.top_left.longitude = 180
a.bounds.bottom_right.latitude = -85
a.bounds.bottom_right.longitude = -180
a.settings.flight_class = flights_pb2.FlightClass.FLIGHT_CLASS_ECONOMY
a.settings.passengers.adults = 1
a.settings.price_bounds.high = 500
a.settings.bags.carry_on_bags = 1
a.settings.inout_bound_settings.outbound.stops = flights_pb2.Stops.STOPS_NON_STOP
a.settings.inout_bound_settings.outbound.date = '2022-06-02'
a.settings.inout_bound_settings.outbound.duration.max_flight_duration = 12 * 60
a.settings.inout_bound_settings.inbound.stops = 1
a.settings.inout_bound_settings.inbound.date = '2022-06-06'
a.settings.inout_bound_settings.inbound.duration.max_flight_duration = 12 * 60
a.settings.flights_only = flights_pb2.FlightOnly.FLIGHT_ONLY_YES
print(a)

def protobuf2array(obj):
    result = []
    for field in obj.DESCRIPTOR.fields:
        val, pos = getattr(obj, field.name), field.number - 1
        while pos > len(result):
            # fill array for not implemented message properties
            result.append(None)
        
        if field.type == field.TYPE_MESSAGE:
            val = protobuf2array(val)
        
        result.append(val)
    print(obj.DESCRIPTOR.name, "result:", result)
    return result

from pprint import pprint
#pprint([(i.name, i.number) for i in a.DESCRIPTOR.fields])
protobuf2array(a)