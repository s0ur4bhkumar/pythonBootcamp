import random
from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def Home():
    rand_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=rand_number, year=year)


@app.route("/<name>")
def get_gender(name):
    response = requests.get("https://api.genderize.io", params={"name": name})
    data = response.json()
    return render_template(
        "index.html",
        name=data["name"],
        probability=int(data["probability"]),
        gender=data["gender"],
    )


if __name__ == "__main__":
    app.run(debug=True)
