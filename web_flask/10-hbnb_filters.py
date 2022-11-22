#!/usr/bin/python3
"""
Start a Flask web application
Listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display HTML page
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)

@app.teardown_appcontext
def tear_down(exception):
    """Close current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
