# A2 – Eigen playbook-experiment (Webserver Nginx)

## Doel
Dit experiment toont hoe met **Ansible** automatisch een **Nginx webserver** wordt geïnstalleerd en geconfigureerd.
Het playbook vervangt de standaardpagina door een eigen HTML-bericht.

## Context
* **Omgeving:** DEVASC VM / Localhost
* **Doel:** De lokale machine (localhost)
* **Ansible connectie:** Lokaal (geen SSH wachtwoord nodig voor localhost in deze setup)

## Bestanden in deze map
* **`hosts`**: Inventory bestand (wijst naar localhost).
* **`ansible.cfg`**: Lokale Ansible configuratie.
* **`install_nginx.yml`**: Het playbook dat Nginx installeert en de HTML-pagina plaatst.
* **`README.md`**: Deze documentatie.

## Wat doet het playbook?
Het playbook voert automatisch de volgende 4 taken uit (zoals gedefinieerd in de code):
1. **Update software lijst:** Voert `apt update` uit.
2. **Installeer Nginx:** Installeert de `nginx` package (state: latest).
3. **Start Nginx:** Zorgt dat de service draait en automatisch start bij boot (enabled).
4. **Maak eigen pagina:** Overschrijft `/var/www/html/index.html` met de tekst: *"Dit is Nginx (Opdracht A2) - En Apache is nu weg!"*

## Playbook uitvoeren

1. Ga naar de map:
   ```bash
   cd ~/labs/"Opdrachten devops"/Ansible/A2_Nginx
