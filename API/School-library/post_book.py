import requests
import json

# Instellingen
BASE_URL = "http://library.demo.local/api/v1"
USER = "cisco"
PASS = "Cisco123!"

# 1. Authenticatie (Token ophalen)
print("--- Inloggen... ---")
auth_response = requests.post(f"{BASE_URL}/loginViaBasic", auth=(USER, PASS))
token = auth_response.json()['token']

# 2. Het boek toevoegen
print("--- POST: Boek toevoegen ---")
headers = {"Content-Type": "application/json", "X-API-Key": token}

nieuw_boek = {
    "id": 150,
    "title": "oefening python",
    "author": "Glenn",
    "isbn": "9781234567897"
}

response = requests.post(f"{BASE_URL}/books", headers=headers, json=nieuw_boek)

print(f"Status Code: {response.status_code}")
print(f"Antwoord server: {response.text}")