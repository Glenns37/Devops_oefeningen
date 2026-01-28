# Pf3 – Eigen API Experiment (JSON)

## Doel
In dit experiment (Pf3) bouwen we een **REST API endpoint**.
In tegenstelling tot Pf1 en Pf2, geeft deze applicatie geen HTML-pagina terug, maar **JSON-data**. Dit is de standaard manier waarop moderne microservices met elkaar praten.

## Context
* **Poort:** 5053
* **Techniek:** `jsonify` module om Python dictionaries om te zetten naar JSON.
* **Type:** API Microservice.

## Bestanden
* **`app.py`**: De Python code die de JSON API draait.
* **`README.md`**: Deze documentatie.
* *(Geen `templates` map nodig, want we gebruiken geen HTML).*

## Vereisten
* Python 3
* Flask (`pip3 install flask`)

## Gebruik

### 1. Applicatie Starten
Ga naar de map `Pf3_Eigen` en start het script:
```bash
python3 app.py
