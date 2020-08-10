Table of Contents
- [Routes](#routes)
  - [states](#states)
  - [state](#state)
  - [city](#city)
  - [station](#station)
  - [data](#data)
    - [Supported Criterion](#supported-criterion)

## Routes 

| Route                     | Method |             Payload/Parameter             | Returns                                                          |
| :------------------------ | :----: | :---------------------------------------: | :--------------------------------------------------------------- |
| /api/states               | `GET`  |                     -                     | list of all states                                               |
| /api/state/api/`<state>`  | `GET`  |                state name                 | list of cities in given state                                    |
| /api/city/api/`<city>`    | `GET`  |                 city name                 | list of stations and their in a given city                       |
| /api/station/api/`<s_id>` | `GET`  |                station id                 | list of parameters available from selected station and their ids |
| /api/data                 | `POST` | from_date, to_date, station_id, criterion | Data from selected station                                       |


### states

```json
GET /api/states

{
    "states" : ["Andhra Pradesh","Delhi"]
}

200 OK
```

### state

```json
GET /api/state/Bihar

{
    "cities": ["Gaya", "Hajipur", "Muzaffarpur", "Patna"],
    "state": "Bihar"
}

200 OK
```

### city

```json
GET /api/city/Patna

{
    "city": "Patna",
    "stations": [{
                    "id": "site_5336",
                    "live": true,
                    "name": "DRM Office Danapur, Patna - BSPCB"
                 },
                 {
                    "id": "site_5335",
                    "live": true,
                    "name": "Govt. High School Shikarpur, Patna - BSPCB"
                 },
                 {
                    "id": "site_157",
                    "live": true,
                    "name": "IGSC Planetarium Complex, Patna - BSPCB"
                 },
                ]
}

200 OK
```

### station

```json
GET /api/station/site_273

{
  "parameters": ["PM2.5", "PM10", "RH", "VWS", "BP", "SR", "AT", "WS", "WD", "CO", "SO2", "Ozone", "NO2", "NO", "NOx", "Benzene", "Xylene", "Toluene"],
  "station": "Ardhali Bazar, Varanasi - UPPCB",
  "station_id": "site_273"
}

```

### data

```json
POST /api/data
Content-Type: application/json

{ 
    "from_date": "01-01-2018 T00:00:00Z",
    "to_date": "02-01-2018 T00:00:00Z",
    "criteria": "24 Hours",
    "station_id": "site_292"
}

200 OK
{
    "data":[{
        "to_date":"....",
        "param_<id>_<name>":"..."
    },
    {
        ...
    },
            ]
}

---
422 Unprocessible Entry
{
    "error_type": "payload_error", 
    "error_message:<"missing payload" | "missing payload param">
} 
```

- The `from_date` and `to_date` are provided as [ISO Format Timestamp](https://en.wikipedia.org/wiki/ISO_8601)

#### Supported Criterion
- 24 Hours
- 8 Hours
- 4 Hours
- 1 Hours
- 30 Minute
- 25 Minute
