#!/bin/bash

 # Active l'environnement virtuel 
source  source myvenv/bin/activate

# Exécution des scripts Bash toutes les 3 heures

# Script bash 
bash event/event_bash.sh
bash football/performance_sportive_bash.sh


# Script Python
python event/summarize_event.py.py
python football/summarize_performance_sportive.py

