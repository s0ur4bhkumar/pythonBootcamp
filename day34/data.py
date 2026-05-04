import requests

data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data.raise_for_status()
question_data = data.json()["results"]


if __name__ == '__main__':
    print(question_data)
