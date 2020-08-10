import json
import base64
import logging
import os
from typing import Dict, List, Union


import requests

from .settings import states, cities, parameters, stations, poll_data

logger = logging.getLogger(__name__)


def get_states() -> List[str]:
    return [state["name"] for state in states.find({})]


def get_cities(state: str) -> List[str]:
    city_dict = cities.find_one({"stateName": state})["citiesInState"]
    return [city["name"] for city in city_dict]


def get_stations(city: str) -> Dict[str, str]:
    return stations.find_one({"cityName": city})["stationsInCity"]


def get_station_names(city: str) -> List[str]:
    station_dict = _get_stations(city=city)
    return [station["name"] for station in station_dict]


def get_station_id(s_name: str) -> List[str]:
    queried = stations.find_one(
        dict(stationsInCity={'$elemMatch': dict(name=s_name)}))
    return queried['stationsInCity'][0]['id']


def _city_state(city: str) -> str:
    """
    Reverse lookup state name from city name
    """
    queried = cities.find_one(
        dict(citiesInState={'$elemMatch': dict(name=city)}))
    return queried['stateName']


def get_station_name(station_id: str) -> str:
    """
    Reverse lookup station name from station id
    """
    queried = stations.find_one(
        dict(stationsInCity={'$elemMatch': dict(id=station_id)}))
    return queried['stationsInCity'][0]['name']


def get_station_city(station_id: str) -> str:
    """
    Reverse lookup city from station id
    """
    queried = stations.find_one(
        dict(stationsInCity={'$elemMatch': dict(id=station_id)}))
    return queried['cityName']


def get_params(station_id: str) -> Union[list, list]:
    param = parameters.find_one({"station_id": station_id})["parameters"]
    ids = []
    names = []
    for p in param:
        ids.append(p["id"])
        names.append(p["name"])
    return ids, names


def construct_payload(**kwargs) -> bytes:
    r = {}
    s_id = kwargs.get("station_id")
    s_name = _s_id_sname(s_id=s_id)
    city = _s_id_city(s_id=s_id)
    state = _city_state(city=city)
    ids, params = get_params(station_id=s_id)
    r["criteria"] = kwargs.get("criteria")
    r["reportFormat"] = "Tabular"
    r["fromDate"] = kwargs.get("from_date")
    r["toDate"] = kwargs.get("to_date")
    r["addedStations"] = [{}]
    r["addedStations"][0]["state"] = state
    r["addedStations"][0]["city"] = city
    r["addedStations"][0]["parameter"] = ids
    r["addedStations"][0]["parameterName"] = params
    r["addedStations"][0]["station"] = s_id
    r["addedStations"][0]["stationName"] = s_name
    rb = json.dumps(r).encode("utf-8")
    return base64.b64encode(rb)


def request_data(payload: str) -> Dict[object, object]:
    try:
        r = requests.post(
            "https://app.cpcbccr.com/caaqms/comparision_data",
            data=payload)
        if r.status_code == 200 and r.text != "":
            return r.json()
        else:
            raise Exception("Payload Error!")
    except Exception as e:
        print(e)


def get(**kwargs) -> Dict[dict, str]:
    payload = _get_payload(**kwargs)
    return format(request_data(payload))


def format(data: dict):
    d = data["tabularData"]["bodyContent"]
    station = data["siteInfo"]["sites"][0]
    return d, station


def _construct_payload(**kwargs) -> bytes:
    r = {}
    r["criteria"] = kwargs.get("criteria")
    r["reportFormat"] = "Tabular"
    r["fromDate"] = kwargs.get("from_date")
    r["toDate"] = kwargs.get("to_date")
    r["addedStations"] = [{}]
    r["addedStations"][0]["state"] = kwargs.get("state")
    r["addedStations"][0]["city"] = kwargs.get("city")
    r["addedStations"][0]["parameter"] = kwargs.get("parameters")
    r["addedStations"][0]["parameterName"] = kwargs.get("paramnames")
    r["addedStations"][0]["station"] = kwargs.get("station_id")
    r["addedStations"][0]["stationName"] = kwargs.get("station_name")
    rb = json.dumps(r).encode("utf-8")
    return base64.b64encode(rb)


def _get_payload(**kwargs):
    print(kwargs)
    from_date = kwargs.get('from_date')
    to_date = kwargs.get('to_date')
    criteria = kwargs.get('criteria')
    s_id = kwargs.get('station_id')
    city = _s_id_city(s_id=s_id)
    station = _s_id_sname(s_id=s_id)
    state = _city_state(city=city)
    ids, params = get_params(station_id=s_id)
    binary_payload = _construct_payload(criteria=criteria, from_date=from_date,
                                        to_date=to_date, state=state, city=city, station_id=s_id,
                                        station_name=station, parameters=ids, paramnames=params)
    return binary_payload
