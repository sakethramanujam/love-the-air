import os
from pymongo import MongoClient

uri = os.getenv('MONGO_DB_URI')

client = MongoClient(uri)
db = client['cpcb']
parameters = db["parameters"]
stations = db["stations"]
cities = db["cities"]
states = db["states"]


urls = [
    {
        "route": "/state",
        "method": "GET",
        "params": "-",
        "desc": "returns list of states"

    },
    {
        "route": "/state/<state>",
        "method": "GET",
        "params": "state",
        "desc": "list of cities with stations in given state"
    },
    {
        "route": "/city/<city>",
        "method": "GET",
        "params": "city",
        "desc": "list of stations and their ids in city"
    },
    {
        "route": "/station/<s_id>",
        "method": "GET",
        "params": "s_id",
        "desc": "list of parameters and their ids for a given station id"
    },
    {
        "route": "/data",
        "method": "POST",
        "params": "",
        "desc": "data...."
    }


]
