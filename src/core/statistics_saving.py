import json
from datetime import date
from src.p_data import STATISTICS_PATH as path

def read_json():
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save(rate:int):
    data = {
        "ACTIVITY": {},
        "ALL_RATE": {},
        "RATE": {}
    }
    today = str(date.today())

    try:
        data = read_json()
    except FileNotFoundError:
        print("STATISTICS FILE DOES NOT EXIST!")
    except json.JSONDecodeError:
        print("STATISTICAL FILE DECODING ERROR!")

    data["ACTIVITY"][today] = data["ACTIVITY"].get(today, 0) + 1
    if today in data["ALL_RATE"]:
        data["ALL_RATE"][today].append(rate)
    else:
        data["ALL_RATE"][today] = [rate]
    data["RATE"][today] = sum(data["ALL_RATE"][today]) / len(data["ALL_RATE"][today])

    write_json(data)