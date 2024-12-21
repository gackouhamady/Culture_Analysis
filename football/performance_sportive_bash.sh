#!/bin/bash

# Clé API de l'API-Football
export $(grep -v '^#' ../.env | xargs)

API_KEY="$API_KEY_foot"

# URL de base de l'API-Football
BASE_URL="https://api.football-data.org/v4/competitions"

# Paramètres de la requête (ajustez selon vos besoins)
LEAGUE_ID=2021 # Exemple pour la Premier League
START_DATE=$(date -u -d '30 days ago' +%Y-%m-%d) # Par exemple, récupérer les matchs des 30 derniers jours
END_DATE=$(date -u +%Y-%m-%d) # Jusqu'à aujourd'hui

# Nom du fichier avec date et heure
FILENAME="football_past_performance_$(date +%Y%m%d_%H%M%S).json"

# Répertoire de stockage
DIRECTORY="football_data"

# Créer le répertoire s'il n'existe pas
mkdir -p "$DIRECTORY"

# Effectuer la requête et sauvegarder les données
curl -G "$BASE_URL/$LEAGUE_ID/matches" \
  --header "X-Auth-Token: $API_KEY" \
  --data-urlencode "dateFrom=$START_DATE" \
  --data-urlencode "dateTo=$END_DATE" \
  -o "$DIRECTORY/$FILENAME"

# Confirmation de l'exécution
echo "Données des performances sportives passées récupérées et sauvegardées dans $DIRECTORY/$FILENAME"