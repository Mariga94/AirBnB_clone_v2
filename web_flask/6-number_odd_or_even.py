#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, request, escape, render_template
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


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def index_6(n):
    """
    route number template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def index_7(n):
    """
    Display odd or even
    """

    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
