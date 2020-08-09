import os
from pymongo import MongoClient

uri = os.getenv('MONGO_DB_URI') 

client = MongoClient(uri) if uri else MongoClient()
db = client['cpcb'] if uri else client['links']
parameters = db["parameters"]
stations = db["stations"]
cities = db["cities"]
states = db["states"]
poll_data = db["data"]
urls = [
    {
        "route": "/api/states",
        "method": "GET",
        "params": "-",
        "desc": "returns list of states"

    },
    {
        "route": "/api/state/<state>",
        "method": "GET",
        "params": "state",
        "desc": "list of cities with stations in given state"
    },
    {
        "route": "/api/city/<city>",
        "method": "GET",
        "params": "city",
        "desc": "list of stations and their ids in city"
    },
    {
        "route": "/api/station/<s_id>",
        "method": "GET",
        "params": "s_id",
        "desc": "list of parameters and their ids for a given station id"
    },
    {
        "route": "/data",
        "method": "POST",
        "params": "from_date, to_date, station_id","criteria"
        "desc": "data...."
    }


]
