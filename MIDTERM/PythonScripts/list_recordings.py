import requests
from config import HEADERS

url = "https://webexapis.com/v1/recordings"

response = requests.get(url, headers=HEADERS)

print(response.status_code)
print(response.text)
