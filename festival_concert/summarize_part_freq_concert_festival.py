import os
import json
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb+srv://hamadygackou777:root@cluster0.1lwk5.mongodb.net/')
db = client['Dashboard_Data_Science']
collection = db['billet_frequent_concert_festival']

# Répertoire contenant les fichiers JSON
directory = 'part_frequent_data'

# Fonction pour résumer les données
def summarize_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        # Sélectionner les attributs pertinents
        summary = []
        for event in data['_embedded']['events']:
            venue_info = event['_embedded'].get('venues', [{}])[0]
            ticket_info = event.get('priceRanges', [{}])[0]
            attendance_info = event.get('attendance', 'NA')
            summary.append({
                'name': event.get('name'),
                'date': event['dates']['start'].get('localDate'),
                'venue': venue_info.get('name', 'NA'),
                'city': venue_info.get('city', {}).get('name', 'NA'),
                'country': venue_info.get('country', {}).get('name', 'NA'),
                'min_ticket_price': ticket_info.get('min', 'NA'),
                'max_ticket_price': ticket_info.get('max', 'NA')
                 
            })
        
        return summary

# Parcourir les fichiers dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        # Résumer les données
        summary = summarize_data(file_path)
        
        # Insérer ou mettre à jour le résumé dans MongoDB
        for event in summary:
            query = {'name': event['name'], 'date': event['date'], 'venue': event['venue']}
            update = {'$set': event}
            collection.update_one(query, update, upsert=True)
        
        # Supprimer le fichier après insertion/mise à jour
        os.remove(file_path)

print("Données résumées et stockées dans MongoDB avec succès.")