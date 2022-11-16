import os

from flask import Flask

from hello_world import say_hello

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """
    Test connection to app.

    :return: Successful connection message
    """
    return "Connected"


@app.route("/hello/<name>")
def hello(name: str):
    """
    Says hello!

    :param name: Name to say hello to

    :return: Hello text
    """
    return say_hello(name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("FLASK_PORT")))
