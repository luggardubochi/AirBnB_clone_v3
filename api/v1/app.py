#!/usr/bin/python3
"""Flask app module"""
from flask import Flask, request
from models import storage
from api.v1.views import app_views
from flask import make_response, jsonify
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def tear_down(exception):
    """Release Resources"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Not found"""
    error_json = {'error': 'Not found'}
    return make_response(jsonify(error_json), 404)


if __name__ == "__main__":
    HOSTS = getenv('HBNB_API_HOST', '0.0.0.0')
    PORTS = getenv('HBNB_API_PORT', '5000')
    app.run(host=HOSTS, port=int(PORTS), threaded=True)
