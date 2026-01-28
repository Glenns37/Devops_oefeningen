# Ap4 - Eigen API Experiment 2 (Webforms)

## Beschrijving
Dit experiment toont hoe Python gebruikersinvoer kan verwerken via een webformulier.
In tegenstelling tot Ap3 (JSON), gebruikt dit project **HTML Templates** en verwerkt het **POST requests** vanuit de browser.

## Onderdelen
* **form_app.py**: De Python applicatie die luistert naar webverzoeken.
* **templates/feedback.html**: De HTML-pagina met het invulformulier.

## Functionaliteit
1. De gebruiker ziet een HTML-formulier (GET request).
2. De gebruiker vult naam en bericht in en klikt op "Verstuur".
3. Python vangt de data op (POST request) en toont deze direct op het scherm.

## Gebruik

### 1. Start de applicatie
Zorg dat je in de map `Ap4_Webforms` staat:
```bash
python3 form_app.py
