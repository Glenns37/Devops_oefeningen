import requests
import json

BASE_URL = "http://library.demo.local/api/v1"
BOEK_ID = 150

print(f"--- GET: Boek {BOEK_ID} ophalen ---")
response = requests.get(f"{BASE_URL}/books/{BOEK_ID}")

print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print("Boek niet gevonden.")