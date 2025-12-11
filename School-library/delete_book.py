import requests

BASE_URL = "http://library.demo.local/api/v1"
USER = "cisco"
PASS = "Cisco123!"
BOEK_ID = 150

# 1. Authenticatie
auth_response = requests.post(f"{BASE_URL}/loginViaBasic", auth=(USER, PASS))
token = auth_response.json()['token']

# 2. Het boek verwijderen
print(f"--- DELETE: Boek {BOEK_ID} verwijderen ---")
headers = {"X-API-Key": token}
response = requests.delete(f"{BASE_URL}/books/{BOEK_ID}", headers=headers)

print(f"Status Code: {response.status_code}")