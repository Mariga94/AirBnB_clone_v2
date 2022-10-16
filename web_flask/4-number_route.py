#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, request, escape
import re


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    route to home
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index2():
    """
    route to HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def index_3(text):
    """
    route to C
    """
    return 'C {}'.format(escape(re.sub("_", " ", text)))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def index_4(text):
    """
    route to python
    """
    return 'Python {}'.format(escape(re.sub("_", " ", text)))


@app.route('/number/<int:n>', strict_slashes=False)
def index5(n):
    """
    route number
    """
    return "{} is a number".format(escape(n))


if __name__ == "__main__":
    run(host='0.0.0.0', port=5000)
