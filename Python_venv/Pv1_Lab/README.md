# Pv1 – Python Virtual Environment (venv)

## Doel
Dit experiment demonstreert het nut en gebruik van een **Python Virtual Environment**.
Een "venv" zorgt voor een geïsoleerde omgeving waarin je Python packages kunt installeren zonder dat ze je systeem-Python of andere projecten vervuilen.

## Context
* **Map:** `Pv1_Lab`
* **Venv Naam:** `mijn_venv`
* **Doel:** Isolatie van dependencies (zoals Flask, Pytest, etc.).

## Bestandsstructuur
* **`mijn_venv/`**: De map die alle geïsoleerde Python-bestanden en libraries bevat (bin, lib, etc.).
* **`README.md`**: Deze handleiding.

## Gebruik

### 1. De Environment Aanmaken
*(Dit is al gedaan in dit lab, maar ter referentie)*
```bash
python3 -m venv mijn_venv
