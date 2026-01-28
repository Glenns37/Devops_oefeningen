# School Library API - Python & Shell Scripts

## Beschrijving
Dit project bevat een collectie van Python- en Shell-scripts om te communiceren met de **School Library REST API**.
Het doel is om de werking van HTTP-methoden (**GET, POST, PUT, DELETE**) te demonstreren via zowel code (`requests` library) als command-line tools (`curl`).

De scripts voeren acties uit op de boeken-database van de bibliotheek API.

## Bestandsstructuur
Dit project bevat scripts voor elke CRUD-operatie in twee varianten:

### 1. Python Scripts (`.py`)
Gebruiken de `requests` library om met de API te praten.
* **`add100RandomBooks.py`**: Voegt automatisch 100 willekeurige boeken toe met behulp van de `Faker` library.
* **`get_book.py`**: Haalt informatie op over boeken (HTTP GET).
* **`post_book.py`**: Voegt een enkel nieuw boek toe (HTTP POST).
* **`put_book.py`**: Wijzigt de gegevens van een bestaand boek (HTTP PUT).
* **`delete_book.py`**: Verwijdert een boek uit de database (HTTP DELETE).

### 2. Shell Scripts (`.sh`)
Gebruiken `curl` om dezelfde acties uit te voeren via de terminal.
* **`get_book.sh`**: Curl commando voor GET requests.
* **`post_book.sh`**: Curl commando voor POST requests.
* **`put_book.sh`**: Curl commando voor PUT requests.
* **`delete_book.sh`**: Curl commando voor DELETE requests.

## Configuratie & Vereisten

### API Gegevens
* **Base URL:** `http://library.demo.local/api/v1` (of `http://localhost:8080/api/v1`).
* **Authenticatie:**
    * Gebruiker: `cisco`
    * Wachtwoord: `Cisco123!`
    * De scripts loggen eerst in om een Token te verkrijgen.

### Installatie (Python)
Voor de Python scripts zijn de volgende libraries nodig:
```bash
pip3 install requests faker
