#!/usr/bin/python3
"""Starts a Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """Displays an HTML page with states and cities
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(e):
    """Remove current session"""
    storage.close()
