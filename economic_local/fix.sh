#!/bin/bash

# URL de l'API de la Banque Mondiale
WORLD_BANK_URL="http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?date=2013:2022&format=json&per_page=10000"

# Répertoire de stockage des données
ECON_DIRECTORY="economic_data"

# Créer le répertoire s'il n'existe pas
mkdir -p "$ECON_DIRECTORY"

# Initialiser les variables
PAGE=1
TOTAL_PAGES=1
FILE_COUNT=0
CHUNK_SIZE=1000  # Taille des blocs de données à sauvegarder

echo "Démarrage de la récupération des données de la Banque Mondiale..."

# Boucle pour gérer la pagination
while [ $PAGE -le $TOTAL_PAGES ]; do
  echo "Récupération de la page $PAGE..."
  
  # Requête à l'API pour la page actuelle
  RESPONSE=$(curl -s "${WORLD_BANK_URL}&page=$PAGE")

  # Obtenir le nombre total de pages (uniquement à la première itération)
  if [ $PAGE -eq 1 ]; then
    TOTAL_PAGES=$(echo "$RESPONSE" | jq '.[0].totalPages // 1')
    echo "Nombre total de pages à récupérer : $TOTAL_PAGES"
  fi

  # Extraire les données des indicateurs économiques
  DATA=$(echo "$RESPONSE" | jq '.[1]')
  
  # Segmentation et sauvegarde des données en blocs
  while [ $(echo "$DATA" | jq 'length') -gt 0 ]; do
    # Extraire un bloc de données
    PART=$(echo "$DATA" | jq ".[0:$CHUNK_SIZE]")
    # Réduire les données restantes
    DATA=$(echo "$DATA" | jq ".[$CHUNK_SIZE:]")

    # Générer un nom de fichier unique pour chaque bloc
    FILE_COUNT=$((FILE_COUNT + 1))
    FILENAME="world_bank_data_$(date +%Y%m%d_%H%M%S)_part_${FILE_COUNT}.json"
    # Sauvegarder le bloc de données dans un fichier
    echo "$PART" > "$ECON_DIRECTORY/$FILENAME"

    echo "Bloc $FILE_COUNT sauvegardé dans $FILENAME"
  done

  # Passer à la page suivante
  PAGE=$((PAGE + 1))
done

echo "Récupération terminée : $FILE_COUNT fichiers créés dans le dossier $ECON_DIRECTORY."
