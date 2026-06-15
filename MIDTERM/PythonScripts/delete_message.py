import requests
from config import HEADERS

message_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvNzJjZWZmNjAtNjg4YS0xMWYxLWE2MTQtYjNhODEyMjNiZmI1"

url = f"https://webexapis.com/v1/messages/Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvNzJjZWZmNjAtNjg4YS0xMWYxLWE2MTQtYjNhODEyMjNiZmI1"

response = requests.delete(url, headers=HEADERS)

print(response.status_code)

if response.status_code == 204:
    print("Deleted Successfully")
