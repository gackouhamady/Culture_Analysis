#!/bin/bash

# Clé API Ticketmaster
export $(grep -v '^#' ../.env | xargs)

API_KEY="$API_KEY_festival"

# URL de base de l'API Ticketmaster
BASE_URL="https://app.ticketmaster.com/discovery/v2/events.json"

# Paramètres de la requête
START_DATE=$(date -u -d '8 hours ago' +%Y-%m-%dT%H:%M:%SZ)
PARAMS="keyword=concert,festival&apikey=$API_KEY&sort=date,desc&startDateTime=$START_DATE"

# Nom du fichier avec date et heure
FILENAME="events_data_$(date +%Y%m%d_%H%M%S).json"

# Répertoire de stockage
DIRECTORY="part_frequent_data"

# Créer le répertoire s'il n'existe pas
mkdir -p "$DIRECTORY"

# Effectuer la requête et sauvegarder les données
curl -G "$BASE_URL" \
  --data-urlencode "keyword=concert,festival" \
  --data-urlencode "apikey=$API_KEY" \
  --data-urlencode "sort=date,desc" \
  --data-urlencode "startDateTime=$START_DATE" \
  -o "$DIRECTORY/$FILENAME"

# Confirmation de l'exécution
echo "Données des événements récupérées et sauvegardées dans $DIRECTORY/$FILENAME"