import requests
from config import HEADERS

url = "https://webexapis.com/v1/messages"

data = {
    "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMGIzZjkyYzAtNjg4OS0xMWYxLTkxYWUtYjk1ZjBhMjFhODI0",
    "text": "Hello from Python"
}

response = requests.post(url, headers=HEADERS, json=data)

print("Status Code:", response.status_code)

result = response.json()

print("Message ID:", result["id"])
print("Message Text:", result["text"])
