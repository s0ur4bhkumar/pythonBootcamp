import datetime as dt
import os

import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_API = os.getenv("SHEETY_API")
BASE_URL = "https://app.100daysofpython.dev"
Authorization_key = os.getenv("Authorization")

headers = {"x-app-id": APP_ID, "x-app-key": API_KEY, "Authorization": Authorization_key}


def post_data():
    exercise_text = str(input("Tell me which exercise you did: "))
    data = {
        "query": exercise_text,
        "gender": "male",
        "weight_kg": 68,
        "age": 24,
        "height_cm": 165,
    }
    POST_REQUEST_URL = f"{BASE_URL}/v1/nutrition/natural/exercise"
    response = requests.post(url=POST_REQUEST_URL, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["exercises"]


def get_data():
    GET_REQUEST_URL = f"{BASE_URL}/healthz"
    response = requests.get(GET_REQUEST_URL)
    response.raise_for_status()
    print(response.text)


def get_sheety_data():
    response = requests.get(url=str(SHEETY_API))
    response.raise_for_status()
    print(response.json())


def post_sheety_data():
    date = dt.datetime.now().date().strftime("%Y/%m/%d")
    time = dt.datetime.now().time().strftime("%H:%M:%S")
    workout_data = post_data()[0]
    print(workout_data)
    exercise = workout_data["name"]
    duration = workout_data["duration_min"]
    calories = workout_data["nf_calories"]
    data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=str(SHEETY_API), json=data, headers=headers)
    print(response.text)
    response.raise_for_status()
    print("response.status_code: ", response.status_code)


post_sheety_data()
