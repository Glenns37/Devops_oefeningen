# A3 - Ansible Database Experiment

## Beschrijving
In dit experiment (A3) gebruiken we **Ansible** om een **MariaDB** database server te installeren op de localhost.
Dit toont aan dat Ansible voor verschillende soorten infrastructuur (niet alleen webservers) gebruikt kan worden.

## Bestanden
* `install_db.yml`: De Playbook die `mariadb-server` installeert en start.
* `hosts`: De inventory file die de localhost definieert als database-server.
* `ansible.cfg`: Configuratie.

## Installatie & Gebruik
1. Run de playbook:
   ```bash
   ansible-playbook install_db.yml
