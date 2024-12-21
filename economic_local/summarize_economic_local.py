import os
import json
from pymongo import MongoClient
from datetime import datetime

# Connexion à MongoDB
client = MongoClient('mongodb+srv://hamadygackou777:root@cluster0.1lwk5.mongodb.net/')
db = client['Dashboard_Data_Science']
collection = db['economic_data']

# Répertoire contenant les fichiers JSON
directory = 'economic_data'

# Fonction pour résumer les données
def summarize_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        # Sélectionner les attributs pertinents
        summary = []
        for entry in data:
            summary.append({
                'country': entry['country']['value'],
                'country_id': entry['country']['id'],
                'country_iso3': entry['countryiso3code'],
                'indicator': entry['indicator']['value'],
                'indicator_id': entry['indicator']['id'],
                'date': entry['date'],
                'value': entry['value']
            })
        
        return summary

# Parcourir les fichiers dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        # Résumer les données
        summary = summarize_data(file_path)
        
        # Insérer ou mettre à jour le résumé dans MongoDB
        for entry in summary:
            query = {'country': entry['country'], 'indicator': entry['indicator'], 'date': entry['date']}
            update = {'$set': entry}
            collection.update_one(query, update, upsert=True)
        
        # Supprimer le fichier après insertion/mise à jour
        os.remove(file_path)

print("Données résumées et stockées dans MongoDB avec succès.")