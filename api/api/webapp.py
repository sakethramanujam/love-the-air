from flask import Flask, request, jsonify
from .db import *
from .settings import urls
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify(
        {"name": "Air Quality Index Data",
         "source": "CPCB CCR",
         "howto": "/api"

         })


@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        "urls": urls
    })


@app.route('/states', methods=['GET'])
def states():
    return jsonify({"states": get_states()})


@app.route('/state/<state>', methods=['GET'])
def state(state):
    return jsonify({
        "state": state,
        "cities": get_cities(state=state)})


@app.route('/city/<city>', methods=['GET'])
def stations(city):
    return jsonify({
        "city": city,
        "stations": get_stations(city=city)
    })


@app.route('/station/<s_id>', methods=['GET'])
def parameters(s_id):
    _, params = get_params(station_id=s_id)
    station = s_id_sname(s_id=s_id)
    return jsonify({
        "station":station,
        "station_id": s_id,
        "parameters": params,
    })


@app.route('/data', methods=['POST'])
def get_data():
    d = request.json
    if not d:
        raise Exception(
            'empty_payload',
        )
    data, station = get(**d)
    return jsonify(
        {"station": station,
            "data": data
         }
    )
