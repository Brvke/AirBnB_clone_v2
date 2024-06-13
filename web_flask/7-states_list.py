#!/usr/bin/python3
"""
A simple Flask web application that lists all State objects from the database.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Route handler for /states_list URL"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('states_list.html', states=states)

@app.teardown_appcontext
def down_db(exception):
    """Method to handle app teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
