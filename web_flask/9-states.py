#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_state():
    """Displays a list of cities in their states in a website"""
    state_list = storage.all(State).values()
    return render_template('7-states_list.html', state_list=state_list)


@app.route('/states/<id>', strict_slashes=False)
def list_state_and_cities(id):
    """Displays a list of cities in their states in a website"""
    state_list = storage.all(State).values()
    found = False
    state = None
    for st in state_list:
        if id in st.id:
            found = True
            state = st
            break
    return render_template('9-states.html', state=state, found=found)


@app.teardown_appcontext
def close_storage(db):
    """Closes the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
