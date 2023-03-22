#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def list_state():
    """Displays a list of cities in their states in a website"""
    state_list = storage.all(State).values()
    amenity_list = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', state_list=state_list,
                           amenity_list=amenity_list)


@app.teardown_appcontext
def close_storage(db):
    """Closes the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
