import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/blog")
def get_blog():
    response = requests.get(" https://api.npoint.io/026e6d8fc172d79aa0a3")
    posts = response.json()
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
