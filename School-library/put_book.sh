#!/bin/bash
URL="http://library.demo.local/api/v1"
USER="cisco"
PASS="Cisco123!"

# Token ophalen
TOKEN=$(curl -s -X POST -u "$USER:$PASS" "$URL/loginViaBasic" | python3 -c "import sys, json; print(json.load(sys.stdin)['token'])")

echo "--- PUT: Boek aanpassen ---"
curl -v -X PUT \
     -H "Content-Type: application/json" \
     -H "X-API-Key: $TOKEN" \
     -d '{"id": 200, "title": "bash oefening 2", "author": "Glenn", "isbn": "9781234567897"}' \
     "$URL/books/200"