import requests
from config import HEADERS

url = "https://webexapis.com/v1/memberships"

data = {
    "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMGIzZjkyYzAtNjg4OS0xMWYxLTkxYWUtYjk1ZjBhMjFhODI0",
    "personEmail": "reydendetanoy46@gmail.com"
}

response = requests.post(url, headers=HEADERS, json=data)

print(response.status_code)
print(response.text)
