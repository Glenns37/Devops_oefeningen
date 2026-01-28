# Pf2 – Flask Login Experiment

## Doel
Dit experiment demonstreert hoe je met **Python Flask** gebruikersinvoer verwerkt.
We bouwen een eenvoudig inlogsysteem dat onderscheid maakt tussen **GET requests** (pagina tonen) en **POST requests** (data versturen).

## Context
* **Poort:** 5052
* **Techniek:** `render_template` voor HTML en `request.form` voor het uitlezen van data.
* **Credentials:** Hardcoded in de Python logica.

## Bestandsstructuur
Flask vereist een specifieke structuur voor HTML-bestanden:
* **`app.py`**: De applicatie logica.
* **`templates/login.html`**: Het HTML-formulier (moet in de map `templates` staan!).
* **`README.md`**: Deze documentatie.

## Vereisten
* Python 3
* Flask (`pip3 install flask`)

## Gebruik

### 1. Applicatie Starten
Ga naar de map `Pf2_Logon` en start het script:
```bash
python3 app.py
