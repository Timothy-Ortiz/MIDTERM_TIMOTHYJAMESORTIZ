import requests
from config import HEADERS

url = "https://webexapis.com/v1/meetings"

payload = {
    "title": "DevOps Webex Midterm Meeting 2",
    "start": "2026-06-20T14:00:00Z",
    "end": "2026-06-20T15:00:00Z",
    "enabledAutoRecordMeeting": False,
    "allowanyUserToBeCoHost": True
}

try:
    response = requests.post(url, headers=HEADERS, json=payload)

    print("Status Code:", response.status_code)
    print(response.json())

except Exception as e:
    print("Error:", e)