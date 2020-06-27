Table of Contents
- [Routes](#routes)
- [Example Responses](#example-responses)

## Routes 

|Route|Method|Payload/Parameter|Returns|
|:-|:-:|:-:|:-|
|/states|`GET`|-|list of all states|
|/state/`<state>`|`GET`|state name|list of cities in given state|
|/city/`<city>`|`GET`|city name|list of stations and their in a given city|
|/station/`<s_id>`|`GET`|station id|list of parameters available from selected station and their ids|
|/data|`POST`|from_date(ISO Timestamp), to_date(ISO Timestamp), station_id, criterion|Data from selected station|


## Example Responses

