#!/bin/bash

# Exécution des scripts Bash toutes les 3 heures
./economic_local_bash.sh
./part_freq_concert_festival_bash.sh
./performance_sportive_bash.sh

# Exécution des scripts Python toutes les 4 heures
./summarize_economic_local.py
./summarize_part_freq_concert_festival.py
./summarize_performance_sportive.py