# Pv2 – Python Deployment & Requirements

## Doel
Dit experiment simuleert de **deployment** van een Python applicatie.
In een professionele omgeving installeer je libraries nooit één voor één met de hand. In plaats daarvan gebruik je een **`requirements.txt`** bestand.
Dit project toont hoe je met één script (`install_app.sh`) automatisch een virtual environment aanmaakt en alle benodigde packages in één keer installeert.

## Context
* **Map:** `Pv2_Deployment`
* **Venv Naam:** `deploy_env`
* **Techniek:** Automatisering via Bash en Pip dependency management.

## Bestandsstructuur
* **`install_app.sh`**: Het bash-script dat het hele installatieproces automatiseert.
* **`requirements.txt`**: Een lijst met alle libraries (en versies) die dit project nodig heeft (bijv. `flask`, `requests`).
* **`deploy_env/`**: De virtual environment die door het script wordt aangemaakt (bevat de geïnstalleerde libraries).
* **`README.md`**: Deze handleiding.

## Gebruik

### 1. Bekijk de requirements (Optioneel)
Kijk wat er geïnstalleerd gaat worden:
```bash
cat requirements.txt
