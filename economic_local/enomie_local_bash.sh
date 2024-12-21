#!/bin/bash

WORLD_BANK_URL="http://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?date=2013:2022&format=json&per_page=10000"

ECON_DIRECTORY="economic_data"

mkdir -p "$ECON_DIRECTORY"   

PAGE=1
TOTAL_PAGES=1
COUNT=0

while [ $PAGE -le $TOTAL_PAGES ]; do
  RESPONSE=$(curl -s "$WORLD_BANK_URL&page=$PAGE")
  TOTAL_PAGES=$(echo $RESPONSE | jq '.[0].totalPages // 1')
  DATA=$(echo $RESPONSE | jq '.[1]')
  
  while [ $(echo $DATA | jq 'length') -gt 0 ]; do
    PART=$(echo $DATA | jq '.[0:1000]')
    DATA=$(echo $DATA | jq '.[1000:]')
    COUNT=$((COUNT + 1))
    FILENAME="world_bank_data_$(date +%Y%m%d_%H%M%S)_part_$COUNT.json"
    echo $PART > "$ECON_DIRECTORY/$FILENAME"
  done

  PAGE=$((PAGE + 1))
done
