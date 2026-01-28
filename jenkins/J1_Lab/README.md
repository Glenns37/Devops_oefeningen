# J1 – Jenkins CI/CD Pipeline Lab

## Doel
Dit experiment demonstreert hoe **Jenkins** gebruikt wordt om het software-ontwikkelproces te automatiseren (CI/CD).
In plaats van handmatig Docker commando's te typen, gebruiken we een **Pipeline Script** om de applicatie te bouwen, te testen en te "deployen".

## Bestandsstructuur
* **`sample_app.py`**: De eenvoudige Python Flask webapplicatie.
* **`Dockerfile`**: Het recept om de applicatie in een container te verpakken.
* **`pipeline_script.groovy`**: **Het belangrijkste bestand!** Dit bevat de stappen die Jenkins moet uitvoeren (Build, Test, Deploy).
* **`sample-app.sh`**: Een bash script om de app lokaal te bouwen en te starten (zonder Jenkins).
* **`templates/` & `static/`**: De HTML en CSS bestanden voor de webpagina.
* **`tempdir/`**: Een tijdelijke map die tijdens het bouwproces wordt aangemaakt (om bestanden naar de container te kopiëren).

## Hoe werkt het?
De pipeline (gedefinieerd in het `.groovy` bestand) voert de volgende stappen automatisch uit:
1.  **Preparation**: Maakt tijdelijke mappen aan en kopieert bestanden.
2.  **Build**: Gebruikt de `Dockerfile` om een image te bouwen.
3.  **Run**: Start de container op de achtergrond.

## Gebruik (In Jenkins)

### 1. Jenkins Starten
Zorg dat je Jenkins server draait (meestal op poort 8080).
Ga naar `http://localhost:8080`.

### 2. Nieuwe Job Maken
1. Klik op **New Item**.
2. Geef de naam: `J1-Pipeline`.
3. Kies **Pipeline** en klik op OK.

### 3. Script Configureren
1. Scroll naar beneden naar het kopje **Pipeline**.
2. Kies bij Definition: **Pipeline script**.
3. Kopieer de **inhoud** van `pipeline_script.groovy` en plak het in het tekstvak in Jenkins.
4. Klik op **Save**.

### 4. Uitvoeren
Klik in het menu links op **Build Now**.
Je ziet nu "Stage View" verschijnen waarbij de blokjes groen worden als de stappen slagen.

## Lokaal Testen (Zonder Jenkins)
Je kunt het shell-script gebruiken om te testen of de app werkt voordat je hem in Jenkins stopt:

```bash
# Maak het script uitvoerbaar
chmod +x sample-app.sh

# Run het script
./sample-app.sh
