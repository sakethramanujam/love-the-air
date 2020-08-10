from flask import Flask, request, jsonify
from .db import *
from .settings import urls
from .errors import error


app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/', methods=['GET'])
def index():
    return jsonify(
        {"name": "Air Quality Index Data",
         "source": "CPCB CCR",
         "how to": "/api"
         })


@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        "urls": urls
    })


@app.route('/api/states', methods=['GET'])
def states():
    return jsonify({"states": get_states()})


@app.route('/api/state/<state>', methods=['GET'])
def state(state):
    try:
        cities = get_cities(state=state)
        return jsonify({
            "state": state,
            "cities": cities}), 200
    except Exception as e:
        return jsonify(error(err_type="processing-error", err_message=e)), 424


@app.route('/api/city/<city>', methods=['GET'])
def stations(city):
    try:
        stations = get_stations(city=city)
        return jsonify({
            "city": city,
            "stations": get_stations(city=city)
        }), 200
    except Exception as e:
        return jsonify(error(err_type="processing-error", err_message=e)), 424


@app.route('/api/station/<s_id>', methods=['GET'])
def parameters(s_id):
    try:
        station = get_station_name(station_id=s_id)
        _, params = get_params(station_id=s_id)
        return jsonify({
            "station": station,
            "station_id": s_id,
            "parameters": params,
        }), 200
    except Exception as e:
        return jsonify(error(err_type="processing-error", err_message=e)), 424


@app.route('/api/data', methods=['POST'])
def get_data():
    d = request.json
    if not d:
        return jsonify(error(err_type="payload_error",
                             err_message="missing payload")), 422
    if 'from_date' not in d:
        return jsonify(error(err_type="payload_error",
                             err_message="missing from_date")), 422
    if 'to_date' not in d:
        return jsonify(error(err_type="payload_error",
                             err_message="missing to_date")), 422
    if 'station_id' not in d:
        return jsonify(error(err_type="payload_error",
                             err_message="missing station_id")), 422
    if 'criteria' not in d:
        return jsonify(error(err_type="payload_error",
                             err_message="missing criteria")), 422

    data, station = get(**d)
    return jsonify(
        {"station": station,
            "data": data
         }
    ), 200

