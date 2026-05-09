from datetime import datetime
import requests_cache
from dateutil.relativedelta import relativedelta
from flight_search import FlightSearch
from rich import print as prettyPrint

requests_cache.install_cache("flights_data")

today = datetime.now().date()
six_months_from_now = today + relativedelta(months=6)

flights = FlightSearch()
flights_search_data = flights.check_flights(
    origin_city_code="PNQ",
    destination_city_code="CDG",
    from_time=today,
    to_time=six_months_from_now,
)
relevant_flights = (
    flights_search_data["best_flights"] + flights_search_data["other_flights"]
)
prettyPrint(flights_search_data.get('other_flights'))