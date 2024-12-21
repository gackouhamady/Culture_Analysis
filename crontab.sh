#!/bin/bash

# Exécution des scripts Bash toutes les 3 heures
economic_local/economic_local_bash.sh
festival_concert/part_freq_concert_festival_bash.sh
football/performance_sportive_bash.sh

# Exécution des scripts Python toutes les 4 heures
economic_local/summarize_economic_local.py
festival_concert/summarize_part_freq_concert_festival.py
football/summarize_performance_sportive.py
