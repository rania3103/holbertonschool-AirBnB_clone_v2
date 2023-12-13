#!/usr/bin/python3
"""a script that starts a Flask web application
and diplay the states"""
from flask import Flask, render_template
from models import storage
from models.state import State
"""display list of all State objects
present in DBStorage sorted by name (A->Z)"""
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def show():
    """display a HTML page: (inside the tag BODY)"""
    states = list(storage.all(State).values())
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
