# A1 – Ansible Apache & Templates

## Doel
Dit experiment toont hoe je met **Ansible** een **Apache webserver** installeert.
Het bijzondere aan deze oefening is het gebruik van de **Template module**. We kopiëren geen statisch bestand, maar gebruiken een **Jinja2 template** (`.j2`) om dynamische data (zoals de datum en tijd van de server) in de HTML-pagina te verwerken.

## Context
* **Server:** Localhost
* **Webserver:** Apache2
* **Techniek:** Jinja2 templating voor dynamische HTML content.

## Bestanden in deze map
* **`hosts`**: Inventory bestand (wijst naar localhost).
* **`ansible.cfg`**: (Optioneel) Lokale Ansible configuratie.
* **`install_apache.yml`**: Het playbook dat Apache installeert en de template verwerkt.
* **`index.html.j2`**: De bron-template met variabelen zoals `{{ ansible_date_time.date }}` en de kaart van Dilbeek.

## Wat doet het playbook?
1. **Update & Installatie:** Zorgt dat `apache2` is geïnstalleerd (via `apt`).
2. **Service Start:** Zorgt dat Apache draait en enabled is.
3. **Template Deploy:** Pakt het bestand `index.html.j2`, vult de variabelen in (datum/tijd), en plaatst het resultaat als `/var/www/html/index.html`.

## Installatie & Uitvoeren

1. Ga naar de map:
   ```bash
   cd ~/labs/"Opdrachten devops"/A1_Apache

2. Run het playbook:
   ```bash
   ansible-playbook install_apache.yml
