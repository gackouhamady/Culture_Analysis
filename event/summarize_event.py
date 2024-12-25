import os
import json
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb+srv://hamadygackou777:root@cluster0.1lwk5.mongodb.net/')
db = client['Dashboard_Data_Science']
collection = db['event']

# Répertoire contenant les fichiers JSON
directory = 'part_frequent_data'

# Fonction pour extraire tous les attributs possibles, y compris les sous-attributs, en omettant les attributs de valeur nulle ou "NA"
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

# Fonction pour résumer les données en excluant les attributs non pertinents pour l'analyse statistique
def summarize_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        summary = []
        for event in data.get('_embedded', {}).get('events', []):
            event_attributes = extract_attributes(event)
            
            # Exclure les attributs non pertinents pour l'analyse statistique
            relevant_attributes = {
                'name': event_attributes.get('name'),
                'type': event_attributes.get('type'),
                'classificationName': event_attributes.get('classifications', [{}])[0].get('segment', {}).get('name', 'non précisé'),
                'dates': event_attributes.get('dates', {}).get('start', {}).get('localDate'),
                'venue': event_attributes.get('_embedded', {}).get('venues', [{}])[0].get('name'),
                'city': event_attributes.get('_embedded', {}).get('venues', [{}])[0].get('city', {}).get('name'),
                'country': event_attributes.get('_embedded', {}).get('venues', [{}])[0].get('country', {}).get('name'),
                'priceRanges': event_attributes.get('priceRanges', [{}])[0] if event_attributes.get('priceRanges') else None,
                'sales': event_attributes.get('sales', {}).get('public', {}).get('startDateTime')
            }
            
            # Nettoyage des attributs non disponibles
            relevant_attributes = {k: v for k, v in relevant_attributes.items() if v is not None}
            
            summary.append(relevant_attributes)
        
        return summary

# Parcourir les fichiers dans le répertoire
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        # Résumer les données
        summary = summarize_data(file_path)
        
        # Insérer ou mettre à jour le résumé dans MongoDB
        for event in summary:
            query = {'name': event['name'], 'dates': event['dates']}
            update = {'$set': event}
            collection.update_one(query, update, upsert=True)
        
        # Supprimer le fichier après insertion/mise à jour
        os.remove(file_path)

print("Données résumées et stockées dans MongoDB avec succès.")