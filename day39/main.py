from datetime import datetime

from dateutil.relativedelta import relativedelta
from flight_search import FlightSearch
from rich import print as prettyPrint

today = datetime.now().date()
six_months_from_now = today + relativedelta(months=6)

flights = FlightSearch()
flights_search_data = flights.check_flights(
    origin_city_code="PNQ",
    destination_city_code="JFK",
    from_time="2026-06-10",
    to_time="2026-06-23",
)
