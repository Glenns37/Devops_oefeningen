#!/bin/bash

# Configuratie
IMAGE_NAME="sample_app_image"
CONTAINER_NAME="sample_app_container"
LOG_FILE="sample_deploy_log.txt"
PORT="5050"

# Functie om naar scherm én logbestand te schrijven
log() {
    echo "$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

log "--- START DEPLOYMENT SCRIPT ---"

# 1. Opruimen van oude containers (Clean start)
log "Stap 1: Oude containers opruimen..."
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

# 2. Bouwen van de image
log "Stap 2: Docker Image bouwen ($IMAGE_NAME)..."
docker build -t $IMAGE_NAME . >> $LOG_FILE 2>&1

# 3. Starten van de container
log "Stap 3: Container starten op poort $PORT..."
docker run -t -d -p $PORT:$PORT --name $CONTAINER_NAME $IMAGE_NAME

# 4. Wachten en controleren
sleep 3
if [ "$(docker inspect -f '{{.State.Running}}' $CONTAINER_NAME)" = "true" ]; then
    log "SUCCESS: Container '$CONTAINER_NAME' draait succesvol!"
    log "App is bereikbaar op http://localhost:$PORT"
    
    # Extra info loggen zoals gevraagd in de slide
    echo "--- Container Details ---" >> $LOG_FILE
    docker container inspect $CONTAINER_NAME >> $LOG_FILE
else
    log "ERROR: Container is niet gestart. Check de logs."
fi

log "--- EINDE SCRIPT ---"

