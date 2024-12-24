#!/bin/bash

# Arrête le script en cas d'erreur
set -e

# Active l'environnement virtuel
if [ -d "myvenv" ]; then
    source myvenv/bin/activate
else
    echo "Erreur : le répertoire 'myvenv' n'existe pas."
    exit 1
fi

# Exécution des scripts Bash

# Vérifie et exécute le script event_bash.sh
if [ -d "event" ]; then
    cd event
    if [ -f "event_bash.sh" ]; then
        bash event_bash.sh
    else
        echo "Erreur : le script 'event_bash.sh' est introuvable dans le répertoire 'event'."
        exit 1
    fi
    cd ..
else
    echo "Erreur : le répertoire 'event' n'existe pas."
    exit 1
fi

# Vérifie et exécute le script performance_sportive_bash.sh
if [ -d "football" ]; then
    cd football
    if [ -f "performance_sportive_bash.sh" ]; then
        bash performance_sportive_bash.sh
    else
        echo "Erreur : le script 'performance_sportive_bash.sh' est introuvable dans le répertoire 'football'."
        exit 1
    fi
    cd ..
else
    echo "Erreur : le répertoire 'football' n'existe pas."
    exit 1
fi

sleep 10

# Exécution des scripts Python
if [ -d "event" ]; then
    cd event
    if [ -f "summarize_event.py" ]; then
        python summarize_event.py
    else
        echo "Erreur : le script 'summarize_event.py' est introuvable dans le répertoire 'event'."
        exit 1
    fi
    cd ..
else
    echo "Erreur : le répertoire 'event' n'existe pas."
    exit 1
fi

if [ -d "football" ]; then
    cd football
    if [ -f "summarize_performance_sportive.py" ]; then
        python summarize_performance_sportive.py
    else
        echo "Erreur : le script 'summarize_performance_sportive.py' est introuvable dans le répertoire 'football'."
        exit 1
    fi
    cd ..
else
    echo "Erreur : le répertoire 'football' n'existe pas."
    exit 1
fi

# Obtenir la date et l'heure actuelles
now=$(date +"%Y-%m-%d %H:%M:%S")

# Définir l'objet de l'e-mail
email_subject="Email du $now"

# Définir le corps de l'e-mail
email_body="Salut,\n\nCeci est votre tâche planifiée qui fonctionne sur Heroku.\n\nCordialement."

# Envoyer l'e-mail
echo -e "Subject: $email_subject\n\n$email_body" | msmtp --from="Hamady GACKOU" -a default hamadygackou777@gmail.com