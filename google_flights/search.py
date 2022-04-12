import requests
import request_pb2 as proto_request
import enums_pb2 as proto_enums
from protobuf2arr import serialize_msg2arr

class GoogleFlights:
    def __init__(self) -> None:
        self.session = requests.Session()
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
            'origin': "https://www.google.com",
            'referer': "https://www.google.com/",
            'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
            "dnt": "1",
        }
        self.session.headers = headers
        self.session.proxies = {
            "http": "127.0.0.1:8888",
            "https": "127.0.0.1:8888",
        }
        self.session.verify = False
    
    def _make_request(self, request: proto_request.RequestWrapper) -> requests.Response:
        payload = f"f.req={serialize_msg2arr(request)}"
        url = "https://www.google.com/_/TravelFrontendUi/data/travel.frontend.flights.FlightsFrontendService/GetExploreDestinations?hl=en&soc-app=162&soc-platform=1&soc-device=1"
        resp = self.session.post(url, payload)
        return resp

    def search(self) -> str:
        request = proto_request.Request()
        request.bounds.top_left.latitude = 85
        request.bounds.top_left.longitude = 180
        request.bounds.bottom_right.latitude = -85
        request.bounds.bottom_right.longitude = -180
        request.settings.three = 1
        request.settings.flight_class = proto_enums.FlightClass.FLIGHT_CLASS_ECONOMY
        request.settings.date_options.month = 7 # april
        request.settings.date_options.trip_date = proto_enums.TripDate.TRIP_DATE_2_WEEKS
        request.settings.passengers.adults = 2
        request.settings.price_bounds.high = 1000
        request.settings.bags.carry_on_bags = 2
        request.settings.inout_bound_settings.outbound.airport.one.one.airport = 'JFK'
        request.settings.inout_bound_settings.outbound.stops = proto_enums.Stops.STOPS_ONE_OR_LESS
        #request.settings.inout_bound_settings.outbound.date = '2022-06-02'
        request.settings.inout_bound_settings.outbound.duration.max_flight_duration = 12 * 60
        request.settings.inout_bound_settings.inbound.stops = proto_enums.Stops.STOPS_ONE_OR_LESS
        #request.settings.inout_bound_settings.inbound.date = '2022-06-06'
        request.settings.inout_bound_settings.inbound.duration.max_flight_duration = 12 * 60
        request.settings.flights_only = proto_enums.FlightOnly.FLIGHT_ONLY_YES
        
        wrapper = proto_request.RequestWrapper()
        wrapper.payload = serialize_msg2arr(request)
        resp = self._make_request(wrapper)
        return resp.text

if __name__ == "__main__":
    client = GoogleFlights()
    data = client.search()
    print(data)