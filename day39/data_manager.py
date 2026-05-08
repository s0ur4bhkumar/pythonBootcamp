import os

import dotenv
import requests

dotenv.load_dotenv(dotenv.find_dotenv())

class DataManager:
    def __init__(self) -> None:
        self.sheety_url = os.getenv("SHEETY_URL")
        self.header = {"Authorization": os.getenv("SHEETY_AUTHORIZATION")}

    def get_sheety_data(self):
        response = requests.get(url=str(self.sheety_url), headers=self.header)
        response.raise_for_status()
        return response.json()["prices"]
