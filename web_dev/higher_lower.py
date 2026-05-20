import random

from flask import Flask

rand_num = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def Home():
    return '<h1>Guess a number between 0 and 9</h1><img src = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzFpaGM1cXg3Z3RxOHBvem41dWpzdGhuMmI5Y2l6YTU1b3RpdzR3ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378khQxt68syiWJy/giphy.gif" width="500" height="600">'


print(rand_num)


@app.route("/<int:number>")
def correct_guess(number):
    if number == rand_num:
        return "You won"
    elif number < rand_num:
        return "too low"
    else:
        return "too high"


if __name__ == "__main__":
    app.run(debug=True)
