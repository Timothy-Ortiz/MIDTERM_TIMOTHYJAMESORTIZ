import requests
from config import HEADERS

message_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvNzJjZWZmNjAtNjg4YS0xMWYxLWE2MTQtYjNhODEyMjNiZmI1"

url = f"https://webexapis.com/v1/messages/{message_id}"

data = {
    "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMGIzZjkyYzAtNjg4OS0xMWYxLTkxYWUtYjk1ZjBhMjFhODI0",
    "text": "Edited via Python"
}

response = requests.put(url, headers=HEADERS, json=data)

print("Status:", response.status_code)
print(response.text)
