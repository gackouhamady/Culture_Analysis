## Problématique
Comment pouvons-nous concevoir un tableau de bord temps réel intégrant des données sur les événements culturels, les performances sportives (football) et les indicateurs économiques, afin d'analyser l’interaction entre l’activité humaine, l’économie et le sport dans une zone géographique donnée ?

## Importance du sujet
Ce projet vise à démontrer comment des données disparates, mais interdépendantes, peuvent être collectées, analysées et visualisées en temps réel pour révéler des insights significatifs. Dans un monde où les décisions économiques, sociales et organisationnelles s’appuient de plus en plus sur des données actualisées, ce tableau de bord fournit un outil unique pour comprendre l’impact économique et social des événements culturels et sportifs.

## Objectifs concrets
1. **Centraliser et analyser des données multi-sources** : Événements, performances sportives, et indicateurs économiques à partir de différentes API en temps réel.  
2. **Mettre en évidence les interactions potentielles** : Par exemple, l’impact des événements culturels et sportifs sur les indicateurs économiques locaux, ou l’influence des performances sportives sur la popularité des équipes et leurs régions.  
3. **Développer un outil d’aide à la décision** : Un tableau de bord visuel et interactif permettant de suivre et de prévoir les tendances, utile pour les gestionnaires d’événements, les économistes ou les autorités locales.  
4. **Démontrer la faisabilité technique** : Validation du concept avec des scripts d’automatisation et une analyse périodique résumée dans MongoDB, tout en garantissant la pertinence et l’actualité des données affichées.


# API utilisées

## 1. **Ticketmaster API**
   - **Nature** : Temps réel
   - **Contenu des données** : Cette API fournit des informations sur les événements (concerts, festivals, événements sportifs, etc.), telles que :
     - Nom de l'événement
     - Date et heure de l'événement
     - Lieu (salle, stade, etc.)
     - Ville et pays
     - Catégorie d'événement (musique, sport, théâtre, etc.)
     - Informations sur les billets , prix
   - **Périodicité** : Les données sont mises à jour en temps réel, selon la disponibilité des événements et des informations mises à jour par Ticketmaster.
   - **Moyen d’accès aux données** :
     - **API** : Les données sont accessibles via une API RESTful.
     - **Clé API** : Une clé d’API est nécessaire pour l'accès aux données. Cette clé peut être obtenue en s'inscrivant sur le site de Ticketmaster.
   - **Droit de réutilisation des données** :
     - **Conditions d'utilisation** : Les données sont protégées par des droits d’auteur et soumises aux conditions d'utilisation de Ticketmaster. L'utilisation des données est généralement limitée aux applications non commerciales. Pour toute utilisation commerciale (comme la revente ou la diffusion de données à des fins commerciales), une autorisation préalable de Ticketmaster est requise.
     - **Restrictions** : La réutilisation des données pour des projets commerciaux nécessite un accord spécifique avec Ticketmaster.
     - **Volumétrie à prévoir sur une année d’utilisation**:
     La volumétrie dépendra du nombre d'événements suivis, mais en moyenne, cela pourrait représenter des centaines de milliers de requêtes sur une année, avec des pics lors de festivals ou événements majeurs.

## 2. **Football Data API**
   - **Nature** : Temps réel
   - **Contenu des données** : Cette API fournit des données sur les compétitions de football à travers le monde. Les informations incluent :
     - Détails sur les compétitions (nom de la compétition, pays, saison)
     - Résultats des matchs
     - Classements des équipes
     - Statistiques de match (score, possession, tirs, etc.)
   - **Périodicité** : Les données sont mises à jour en temps réel ou très proche du temps réel pendant les matchs. Les résultats des matchs sont ajoutés dès qu'ils sont disponibles.
   - **Moyen d’accès aux données** :
     - **API** : L'accès aux données se fait via une API RESTful.
     - **Clé API** : Une clé API est nécessaire pour authentifier les requêtes. Elle peut être obtenue après inscription sur le site officiel de Football Data.
   - **Droit de réutilisation des données** :
     - **Conditions d'utilisation** : Les données sont fournies sous des conditions d'utilisation spécifiques. En général, les données peuvent être utilisées à des fins personnelles ou académiques. Pour un usage commercial (par exemple, pour une application de paris ou une plateforme commerciale), une licence spécifique est requise.
     - **Restrictions** : L’utilisation des données est limitée dans un cadre non commercial, sauf si un accord commercial est obtenu avec les propriétaires des données.
   - **Volumétrie à prévoir sur une année d’utilisation**:
     Selon le nombre de compétitions suivies et la fréquence des matchs, la volumétrie pourrait être de plusieurs millions de requêtes sur l'année, surtout en période de compétitions majeures (Coupes du Monde, Ligues, etc.).

## 3. **World Bank API**
   - **Nature** : Pas en temps réel (données économiques historiques)
   - **Contenu des données** : Cette API fournit des données économiques détaillées pour différents pays, notamment :
     - PIB par pays (en dollars constants ou courants)
     - Indicateurs économiques comme la population, la croissance économique, les investissements, etc.
     - Données sur la pauvreté, l'accès à l'éducation, la santé, les infrastructures, etc.
     - Ces données couvrent plusieurs décennies, avec des mises à jour périodiques.
   - **Périodicité** : Les données économiques sont mises à jour annuellement ou selon la publication de nouveaux rapports économiques par la Banque Mondiale.
     - Les ensembles de données peuvent couvrir des périodes comme 2013-2022, selon l'indicateur spécifique.
   - **Moyen d’accès aux données** :
     - **API** : L'accès aux données se fait via une API RESTful, sans nécessiter d'authentification.
     - **Téléchargement** : Les données peuvent également être téléchargées en format JSON ou XML pour une utilisation hors ligne.
     - **Token nécessaire** : Aucun token n'est nécessaire pour accéder aux données de l'API.
   - **Droit de réutilisation des données** :
     - **Conditions d'utilisation** : Les données sont ouvertes au public et peuvent être utilisées gratuitement, sous réserve de respect des conditions d'utilisation de la Banque Mondiale. L’attribution est obligatoire si les données sont utilisées dans des publications ou des projets.
     - **Restrictions** : Les données peuvent être utilisées librement dans des projets académiques, de recherche ou d'analyse. Pour un usage commercial, il est recommandé de vérifier les conditions spécifiques sur le site de la Banque Mondiale.
     - **Volumétrie à prévoir sur une année d’utilisation**:
     La volumétrie peut être modeste, en fonction du nombre d'indicateurs suivis, avec des centaines de milliers de points de données à traiter sur l'année.
## 4. **Points communs entre les sources de données**
   - **Accès via API**: Toutes les trois API offrent un accès via des appels RESTful.
   - **Données structurées en JSON** : Les données sont principalement disponibles en format JSON, ce qui facilite leur traitement et leur intégration dans des applications.
  - **Utilisation en temps réel ou périodique** : Les deux premières API (Ticketmaster et Football Data) offrent des données mises à jour en temps réel, tandis que la troisième (World Bank) propose des données historiques mises à jour annuellement.
  - **Nécessité d'une clé API pour deux**: Ticketmaster et Football Data nécessitent une clé API pour accéder aux données, tandis que la Banque Mondiale permet un accès libre sans clé API.
## 5. **Volumétrie à prévoir** :
   - **Ticketmaster API** : La volumétrie dépend des événements suivis, mais elle peut atteindre des centaines de milliers de requêtes par an.
   - **Football Data API :** En raison de la mise à jour en temps réel, cette API peut générer plusieurs millions de requêtes annuellement, selon la fréquence des matchs.
   - **World Bank API**: Cette API génère moins de volumétrie, mais peut contenir des centaines de milliers de points de données par an, selon les indicateurs suivis.


# Importation et Transformation des Données

## 1. API Ticketmaster (Événements)

### Code d'Importation

```bash
#!/bin/bash

# Clé API Ticketmaster
export $(grep -v '^#' ../.env | xargs)

API_KEY="$API_KEY_festival"

# URL de base de l'API Ticketmaster
BASE_URL="https://app.ticketmaster.com/discovery/v2/events.json"

# Paramètres de la requête
START_DATE=$(date -u -d '8 hours ago' +%Y-%m-%dT%H:%M:%SZ)
PARAMS="apikey=$API_KEY&sort=date,desc&startDateTime=$START_DATE"

# Nom du fichier avec date et heure
FILENAME="events_data_$(date +%Y%m%d_%H%M%S).json"

# Répertoire de stockage
DIRECTORY="part_frequent_data"

# Créer le répertoire s'il n'existe pas
mkdir -p "$DIRECTORY"

# Effectuer la requête et sauvegarder les données
curl -G "$BASE_URL" \
  --data-urlencode "apikey=$API_KEY" \
  --data-urlencode "sort=date,desc" \
  --data-urlencode "startDateTime=$START_DATE" \
  -o "$DIRECTORY/$FILENAME"

# Confirmation de l'exécution
echo "Données des événements récupérées et sauvegardées dans $DIRECTORY/$FILENAME" 
```

### Code de Transformation 

```python   
import os
import json
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb+srv://hamadygackou777:root@cluster0.1lwk5.mongodb.net/')
db = client['Dashboard_Data_Science']
collection = db['event']

# Répertoire contenant les fichiers JSON
directory = 'part_frequent_data'

# Fonction pour extraire tous les attributs possibles
def extract_attributes(data):
    attributes = {}
    for key, value in data.items():
        if isinstance(value, dict):
            nested_attributes = extract_attributes(value)
            attributes[key] = nested_attributes
        elif isinstance(value, list):
            if value and isinstance(value[0], dict):
                nested_list = [extract_attributes(item) for item in value]
                attributes[key] = nested_list
            else:
                attributes[key] = value
        else:
            if value not in [None, 'NA']:
                attributes[key] = value
    return attributes

# Fonction pour résumer les données
def summarize_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        summary = []
        for event in data.get('_embedded', {}).get('events', []):
            event_attributes = extract_attributes(event)
            relevant_attributes = {
                'name': event_attributes.get('name'),
                'type': event_attributes.get('type'),
                'dates': event_attributes.get('dates', {}).get('start', {}).get('localDate'),
                'venue': event_attributes.get('_embedded', {}).get('venues', [{}])[0].get('name'),
                'city': event_attributes.get('_embedded', {}).get('venues', [{}])[0].get('city', {}).get('name'),
                'country': event_attributes.get('_embedded', {}).get('venues', [{}])[0].get('country', {}).get('name'),
                'priceRanges': event_attributes.get('priceRanges', [{}])[0] if event_attributes.get('priceRanges') else None,
                'sales': event_attributes.get('sales', {}).get('public', {}).get('startDateTime')
            }
            
            relevant_attributes = {k: v for k, v in relevant_attributes.items() if v is not None}
            summary.append(relevant_attributes)
        
        return summary

# Parcourir les fichiers dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        summary = summarize_data(file_path)
        
        for event in summary:
            query = {'name': event['name'], 'dates': event['dates']}
            update = {'$set': event}
            collection.update_one(query, update, upsert=True)
        
        os.remove(file_path)

print("Données résumées et stockées dans MongoDB avec succès.")

``` 

## 2. API Football

### Code d'importation 
``` bash 
#!/bin/bash

# Clé API de l'API-Football
export $(grep -v '^#' ../.env | xargs)

API_KEY="$API_KEY_foot"

# URL de base de l'API-Football
BASE_URL="https://api.football-data.org/v4/competitions"

# Paramètres de la requête
LEAGUE_ID=2021
START_DATE=$(date -u -d '30 days ago' +%Y-%m-%d)
END_DATE=$(date -u +%Y-%m-%d)

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

```
### Code de Transformation

``` python
import os
import json
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb+srv://hamadygackou777:root@cluster0.1lwk5.mongodb.net/')
db = client['Dashboard_Data_Science']
collection = db['football_past_performance']

# Répertoire contenant les fichiers JSON
directory = 'football_data'

# Fonction pour résumer les données
def summarize_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        summary = []
        for match in data['matches']:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            winner = match['score']['winner']
            
            if winner == 'HOME_TEAM':
                performance_home_team = 'winner'
                performance_away_team = 'loser'
            elif winner == 'AWAY_TEAM':
                performance_home_team = 'loser'
                performance_away_team = 'winner'
            else:
                performance_home_team = 'draw'
                performance_away_team = 'draw'
            
            summary.append({
                'home_team': home_team,
                'away_team': away_team,
                'date': match['utcDate'],
                'status': match['status'],
                'competition': match['competition']['name'],
                'score_home_team': match['score']['fullTime'].get('home', 'NA'),
                'score_away_team': match['score']['fullTime'].get('away', 'NA'),
                'performance_home_team': performance_home_team,
                'performance_away_team': performance_away_team
            })
        
        return summary

# Parcourir les fichiers dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        summary = summarize_data(file_path)
        
        for match in summary:
            query = {'home_team': match['home_team'], 'away_team': match['away_team'], 'date': match['date']}
            update = {'$set': match}
            collection.update_one(query, update, upsert=True)
        
        os.remove(file_path)

print("Données résumées et stockées dans MongoDB avec succès.")

```
## 3. API World Bank 

### Code d'importation 
``` bash 
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

```
### Code de Transformation

 ```python 
import os
import json
from pymongo import MongoClient
import pandas as pd

# Connexion à MongoDB
client = MongoClient('mongodb+srv://hamadygackou777:root@cluster0.1lwk5.mongodb.net/')
db = client['Dashboard_Data_Science']
collection = db['economic_data']

# Répertoire contenant les fichiers JSON
directory = 'economic_data'

# Fonction pour transformer les données en DataFrame
def process_economic_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        records = []
        for record in data:
            records.append({
                'country': record['country']['value'],
                'indicator': record['indicator']['value'],
                'value': record['value'],
                'date': record['date']
            })
        
        return pd.DataFrame(records)

# Fonction pour insérer les données dans MongoDB
def insert_data_to_mongo(dataframe):
    for _, row in dataframe.iterrows():
        record = row.to_dict()
        collection.update_one({'country': record['country'], 'indicator': record['indicator'], 'date': record['date']}, 
                              {'$set': record}, upsert=True)

# Parcourir les fichiers dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        df = process_economic_data(file_path)
        insert_data_to_mongo(df)
        
        os.remove(file_path)

print("Données économiques traitées et stockées dans MongoDB avec succès.")

```
## Fichier Chron : 
``` bash 
#!/bin/bash

 # Active l'environnement virtuel 
source myvenv/bin/activate

# Exécution des scripts Bash toutes les 3 heures

# Script bash 
bash event/event_bash.sh
bash football/performance_sportive_bash.sh


# Script Python
python event/summarize_event.py.py
python football/summarize_performance_sportive.py

```
## Cron Job :  Automatisation du  fichier chron ci dessus 
0 */3 * * *   crontab.sh >>  cron.log 2>&1



















## Exploration de la base de données MongoDB

Pour explorer la base de données, il faut télécharger MongoDB Compass et se connecter à la base avec ce lien :  
`mongodb+srv://<db_username>:<db_password>@cluster0.1lwk5.mongodb.net/`

- **db_username** : `user`  
- **db_password** : `user`


## Cron Job

- 0 */3 * * * /path/vers/crontab.sh


## Configuration et Tests de Scripts Python avec PyMongo et Tâches Cron
- Pour tout problème lié à PyMongo, vous pouvez créer directement un environnement virtuel Python. Dans cet environnement, vous pourrez tester les scripts Python, définir la tâches cron ...  ci  dessus :  (0 */3 * * * /path/vers/crontab.sh)
