#!/usr/bin/python3
""" This script starts a Flask web application """
from models import storage
from flask import render_template


@app.teardown_appcontext
def teardown():
    """ stops a mysql session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """ This method displays all states """
    state = storage.all(States)
    return render_template("7-states_list.html", the_states=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
