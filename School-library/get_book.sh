#!/bin/bash
echo "--- GET: Boek ophalen ---"
curl -s "http://library.demo.local/api/v1/books/200" | python3 -m json.tool