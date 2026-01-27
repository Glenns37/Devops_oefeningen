#!/bin/bash
echo "--- Start Deployment (Pv2) ---"
python3 -m venv deploy_env
source deploy_env/bin/activate

echo "Installeren van dependencies uit requirements.txt..."
pip install -r requirements.txt

echo "Klaar! Geïnstalleerde packages:"
pip list
