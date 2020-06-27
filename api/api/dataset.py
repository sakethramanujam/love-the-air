class Dataset:
    def __init__(self, station, id, filename):
        self.id = id
        self.station = station
        self._filename = os.path.join(DATAPATH, filename)
        self.all_data = self._get_all()
        self.location = self._latlong()

    def __repr__(self):
        return f"<Dataset {label}>"

    @classmethod
    def find(cls, station):
        if station in station_data.keys():
            id, filename = station_data[station]["id"], station_data[station]["filename"]
            return Dataset(
                station=station,
                id=id,
                filename=filename)
        else:
            return None

    def _get_filename(self, station):
        filename = os.path.join(DATAPATH, station_data[station]["filename"])
        return filename

    def _get_all(self):
        with open(self._filename, 'r') as d:
            try:
                data = json.load(d)
                return data
            except KeyError as e:
                logger.warning(f"Station {station} doens't exist")

    def _latlong(self):
        lat = self.all_data[self.station]['lat']
        long = self.all_data[self.station]['long']
        return lat, long

    def frequencies(self):
        f = self.all_data[self.station] ["frequencies"]
        return f

    def data_for_frequency(self, frequency: str):
        data = self.all_data[self.station]["data"][frequency]
        return data

    def data_for_frequency_date(self, date, frequency):
        date_data=self.data_for_frequency(frequency=frequency)
        try:
            return date_data[date]
        except Exception as e:
            logger.warning(f'Failed fetching data requested {e}')
