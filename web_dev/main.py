from flask import Flask


# --------------------------------------Decorator--------------------------------------
def bold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function(*args, **kwargs)}</b>"

    return wrapper


def italic(function):
    def wrapper(*args, **kwargs):
        return f"<em>{function(*args, **kwargs)}</em>"

    return wrapper


def underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function(*args, **kwargs)}</u>"

    return wrapper


# --------------------------------------flask main---------------------------------------

app = Flask(__name__)


@app.route("/")
@bold
@italic
@underline
def hello_world():
    return "Hello world"


@app.route("/username/<name>")
def greet(name):
    return name


if __name__ == "__main__":
    
    # app.run(debug=True)
