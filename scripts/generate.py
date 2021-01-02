import argparse
import os
from api.api import settings, db
import logging
from tqdm import tqdm

stations = settings.stations


def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=str, help="from date", required=True)
    parser.add_argument("-e", "--end", type=str, help="to date", required=True)
    parser.add_argument(
        "-c",
        "--criteria",
        type=str,
        help="supported criterion, '24 Hours', '8 Hours', '1 Hours','30 Minutes', '15 Minutes'",
        required=True,
    )
    parser.add_argument('-p','--path',type=str,help="Path to store payloads")
    return parser.parse_args()


def _get_payloads(
    start: str,
    end: str,
    criteria: str,
    path:str=None,
):
    payloads = [
        db._get_payload(
            station_id=st["id"], from_date=start, to_date=end, criteria=criteria
        )
        for st in station["stationsInCity"]
        for station in stations.find({})
    ]
    file = os.path.join(path,"payloads.txt") or "/tmp/payloads.txt"
    with open(file, "w") as f:
        [f.write(p + "\n") for p in tqdm(payloads)]


def main():
    arguments = getargs()
    start = arguments.start
    end = arguments.end
    criteria = arguments.criteria
    path = arguments.path
    if not path:
        logging.info("File path not supplied, writing to /tmp/payloads.txt")
    _get_payloads(start=start,end=end,criteria=criteria,path=path)


if __name__ == "__main__":
    main()