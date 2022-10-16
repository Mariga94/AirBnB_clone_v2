#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, request


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    route to home
    """
    return 'Hello HBNB!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
