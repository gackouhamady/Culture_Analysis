import os
import webbrowser
import time

# Lancer Streamlit
os.system("streamlit run dashboard.py --server.port 8501")

# Attendre quelques secondes pour s'assurer que le serveur est démarré
time.sleep(5)

# Ouvrir le navigateur
webbrowser.get('chrome').open("http://localhost:8501")