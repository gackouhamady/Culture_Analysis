#!/bin/bash

# Clé API de l'API-Football
export $(grep -v '^#' ../.env | xargs)
API_KEY="$API_KEY_foot"

# URL de base de l'API-Football
BASE_URL="https://api.football-data.org/v4/competitions"

# Liste des compétitions à récupérer 
COMPETITIONS=(2021 2001 2014) 

# Paramètres de la requête (ajustez selon vos besoins)
START_DATE=$(date -u -d '8 hours ago' +%Y-%m-%dT%H:%M:%SZ) # Par exemple, récupérer les matchs des 8 dernières heures
END_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ) # Jusqu'à aujourd'hui

# Répertoire de stockage
DIRECTORY="football_data"

# Créer le répertoire s'il n'existe pas
mkdir -p "$DIRECTORY"

# Boucle sur chaque compétition
for LEAGUE_ID in "${COMPETITIONS[@]}"; do
  # Nom du fichier avec date et heure
  FILENAME="football_${LEAGUE_ID}_past_performance_$(date +%Y%m%d_%H%M%S).json"

  echo "Récupération des données pour la compétition $LEAGUE_ID..."

  # Effectuer la requête et sauvegarder les données
  curl -G "$BASE_URL/$LEAGUE_ID/matches" \
    --header "X-Auth-Token: $API_KEY" \
    --data-urlencode "dateFrom=$START_DATE" \
    --data-urlencode "dateTo=$END_DATE" \
    -o "$DIRECTORY/$FILENAME"

  echo "Données pour la compétition $LEAGUE_ID sauvegardées dans $DIRECTORY/$FILENAME"
done

# Confirmation de l'exécution
echo "Données des performances sportives passées récupérées et sauvegardées dans le dossier $DIRECTORY"