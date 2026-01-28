#!/bin/bash
URL="http://library.demo.local/api/v1"
USER="cisco"
PASS="Cisco123!"

# Token ophalen
TOKEN=$(curl -s -X POST -u "$USER:$PASS" "$URL/loginViaBasic" | python3 -c "import sys, json; print(json.load(sys.stdin)['token'])")

echo "--- DELETE: Boek verwijderen ---"
curl -v -X DELETE -H "X-API-Key: $TOKEN" "$URL/books/200"