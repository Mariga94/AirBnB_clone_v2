#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, request


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return 'Hello HBNB!'
