import os

import dotenv
import requests
from rich import print as prettyPrint

dotenv.load_dotenv(dotenv.find_dotenv())


class FlightSearch:
    def __init__(self) -> None:
        self.api_key = os.getenv("SERP_API")
        self.url = "https://serpapi.com/search"

    def check_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        configs = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": str(from_time),
            "return_date": str(to_time),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.api_key,
        }

        response = requests.get(url=self.url, params=configs)
        response.raise_for_status()
        return response.json()
