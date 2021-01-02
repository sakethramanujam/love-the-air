# :pen: Using `generate.py`

> :warning: This script only gives a plain text file containing base64 encoded payloads for all 231 stations across India, to download the data please use the python [client](https://github.com/sakethramanujam/cpcbccr-python-client) :warning:

The script has following arguments

```text
  -h,       --help                 show this help message and exit
  -s START, --start START          start date in string format eg., 01-01-2020
  -e END,   --end END              end date in string format eg., 31-01-2020
  -c CRITERIA*, --criteria CRITERIA supported criteria:'24 Hours', '8 Hours', '1 Hours','30 Minutes', '15 Minutes'
  -p PATH, --path PATH             Path to store payloads as string
```

> Critiera: determines the recording frequency of the data to be downloaded

## Generic Usage

```bash
$ ./generate.py -s "01-01-2020" -e "31-12-2020" -c "24 Hours" -p ~/payloads
```

## Contents of the output file

```text
eyJjcml0ZXJpYSI6ICIyNCBIb3VycyIsICJyZXBvcnRGb3JtYXQiOiAiVGFidWxhciIsICJmcm9tRGF0ZSI6ICIwMS0wMS0yMDIwIiwgInRvRGF0ZSI6ICIzMS0xMi0yMDIwIiwgImFkZGVkU3RhdGlvbnMiOiBbeyJzdGF0ZSI6ICJEZWxoaSIsICJjaXR5IjogIkRlbGhpIiwgInBhcmFtZXRlciI6IFsicGFyYW1ldGVyXzIxNSIsICJwYXJhbWV0ZXJfMTkzIiwgInBhcmFtZXRlcl8yMDQiLCAicGFyYW1ldGVyXzIzOCIsICJwYXJhbWV0ZXJfMjM3IiwgInBhcmFtZXRlcl8yMzUiLCAicGFyYW1ldGVyXzIzNCIsICJwYXJhbWV0ZXJfMjM2IiwgInBhcmFtZXRlcl8yMjYiLCAicGFyYW1ldGVyXzIyNSIsICJwYXJhbWV0ZXJfMTk0IiwgInBhcmFtZXRlcl8zMTEiLCAicGFyYW1ldGVyXzMxMiIsICJwYXJhbWV0ZXJfMjAzIiwgInBhcmFtZXRlcl8yMjIiLCAicGFyYW1ldGVyXzIwMiIsICJwYXJhbWV0ZXJfMjMyIiwgInBhcmFtZXRlcl8yMjMiLCAicGFyYW1ldGVyXzI0MCIsICJwYXJhbWV0ZXJfMjE2Il0sICJwYXJhbWV0ZXJOYW1lIjogWyJQTTEwIiwgIlBNMi41IiwgIkFUIiwgIkJQIiwgIlNSIiwgIlJIIiwgIldEIiwgIlJGIiwgIk5PIiwgIk5PeCIsICJOTzIiLCAiTkgzIiwgIlNPMiIsICJDTyIsICJPem9uZSIsICJCZW56ZW5lIiwgIlRvbHVlbmUiLCAiWHlsZW5lIiwgIk1QLVh5bGVuZSIsICJFdGgtQmVuemVuZSJdLCAic3RhdGlvbiI6ICJzaXRlXzUwMjQiLCAic3RhdGlvbk5hbWUiOiAiQWxpcHVyLCBEZWxoaSAtIERQQ0MifV19

```

which translates to

```json
{
  "criteria": "24 Hours",
  "reportFormat": "Tabular",
  "fromDate": "01-01-2020",
  "toDate": "31-12-2020",
  "addedStations": [
    {
      "state": "Delhi",
      "city": "Delhi",
      "parameter": [
        "parameter_215",
        "parameter_193",
        "parameter_204",
        "parameter_238",
        "parameter_237",
        "parameter_235",
        "parameter_234",
        "parameter_236",
        "parameter_226",
        "parameter_225",
        "parameter_194",
        "parameter_311",
        "parameter_312",
        "parameter_203",
        "parameter_222",
        "parameter_202",
        "parameter_232",
        "parameter_223",
        "parameter_240",
        "parameter_216"
      ],
      "parameterName": [
        "PM10",
        "PM2.5",
        "AT",
        "BP",
        "SR",
        "RH",
        "WD",
        "RF",
        "NO",
        "NOx",
        "NO2",
        "NH3",
        "SO2",
        "CO",
        "Ozone",
        "Benzene",
        "Toluene",
        "Xylene",
        "MP-Xylene",
        "Eth-Benzene"
      ],
      "station": "site_5024",
      "stationName": "Alipur, Delhi - DPCC"
    }
  ]
}
```


Consider contributing to the project.