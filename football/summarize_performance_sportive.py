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
