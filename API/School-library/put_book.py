import requests
import json

BASE_URL = "http://library.demo.local/api/v1"
USER = "cisco"
PASS = "Cisco123!"
BOEK_ID = 150

# 1. Authenticatie
auth_response = requests.post(f"{BASE_URL}/loginViaBasic", auth=(USER, PASS))
token = auth_response.json()['token']

# 2. Het boek updaten
print(f"--- PUT: Boek {BOEK_ID} titel aanpassen ---")
headers = {"Content-Type": "application/json", "X-API-Key": token}

update_data = {
    "id": BOEK_ID,
    "title": "oefening python (Versie 2.0)",
    "author": "Glenn",
    "isbn": "9781234567897"
}

response = requests.put(f"{BASE_URL}/books/{BOEK_ID}", headers=headers, json=update_data)
print(f"Status Code: {response.status_code}")