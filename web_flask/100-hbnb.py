#!/usr/bin/python3
"""Start Flask web application
listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display HTML page
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    cities = storage.all("City")
    places = storage.all("Place")
    users = storage.all("User")
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, cities=cities,
                           places=places, users=users)


@app.teardown_appcontext
def tear_down(exception):
    """
    Close current SQLALchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
