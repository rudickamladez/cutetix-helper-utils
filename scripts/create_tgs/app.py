import requests
import os

API_URL = os.getenv("API_URL")
TG_CAPACITY = os.getenv("TG_CAPACITY")
EVENT_ID = os.getenv("EVENT_ID")
time_groups_names = [
    "14:00",
    "14:10",
    "14:20",
    "14:30",
    "14:40",
    "14:50",
    "15:00",
    "15:10",
    "15:20",
    "15:30",
    "15:40",
    "15:50",
    "16:10",
    "16:20",
    "16:30",
    "16:40",
    "16:50",
    "17:00",
]

for tg_name in time_groups_names:
    response = requests.post(
        url=API_URL + "/ticket_groups/",
        json={
            "name": tg_name,
            "capacity": TG_CAPACITY,
            "event_id": EVENT_ID
        }
    )
    response_in_json = response.json()
    print(response_in_json["name"])
