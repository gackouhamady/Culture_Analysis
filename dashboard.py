import streamlit as st
import pandas as pd
import plotly.express as px
import pymongo
from datetime import datetime
from dateutil import parser

from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Dashboard : Culture Analysis", page_icon="📊", layout="wide")

# MongoDB connection setup
@st.cache_resource
def connect_to_mongo():
    client = pymongo.MongoClient("mongodb+srv://user:user@cluster0.1lwk5.mongodb.net/")  # Update with your connection string
    db = client["Dashboard_Data_Science"]
    return db

db = connect_to_mongo()

# Load data from MongoDB
@st.cache_data
def load_data():
    event = pd.DataFrame(list(db["event"].find()))
    football = pd.DataFrame(list(db["football"].find()))
    economy = pd.DataFrame(list(db["economic_data"].find()))
    
    # Rename 'dates' column to 'date'
    event = event.rename(columns={"dates": "date"})
    football = football.rename(columns={"dates": "date"})
    economy = economy.rename(columns={"dates": "date"})
    
    return event, football, economy

event, football, economy = load_data()


# Sidebar navigation
# Sidebar avec des icônes spécifiques
import streamlit as st
from streamlit_option_menu import option_menu





# Personnalisation du sidebar
with st.sidebar:
    section = option_menu(
        menu_title="Tableau de bord",  # Titre du menu
        options=["Rapport", "Accueil", "Événements culturels", "Données sportives", "Indicateurs économiques", "Analyse avancée"],  # Section
        icons=["file", "house", "headphones", "trophy", "bar-chart", "graph-up"],  # Icônes correspondantes
        menu_icon="list",  # Icône pour le menu global
        default_index=0,  # Section par défaut
        styles={
            "container": {"padding": "5px", "background-color": "#2E2E2E", "height": "100vh", "display": "flex", "flex-direction": "column", "justify-content": "center"},
            "icon": {"color": "blue", "font-size": "18px"},  # Couleur et taille des icônes
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},  # Couleur de sélection
        },
    )


# Homepage
# Sections
if section == "Rapport":
    st.title("📄 Rapport du Projet ")
    st.markdown("###  Analyse et Visualisation des Données Multi-Sectorielles : Événements, Sports et Économie")

    # Fournir le chemin ou le lien vers le fichier Markdown
    markdown_file_path = "README.md"  

    try:
        # Lire et afficher le contenu du fichier Markdown
        with open(markdown_file_path, "r", encoding="utf-8") as file:
            markdown_content = file.read()
        st.markdown(markdown_content)
    except FileNotFoundError:
        st.error("Le fichier Markdown spécifié n'a pas été trouvé.")
    except Exception as e:
        st.error(f"Une erreur s'est produite lors du chargement du fichier Markdown : {e}")


if section == "Accueil":
    st.title("🏠 Accueil")
    st.write("Bienvenue sur le tableau de bord intégré.")
    # Ajouter des contenus pour l'accueil ici.

    col1, col2, col3 = st.columns(3)
    col1.metric("Événements culturels", len(event))
    col2.metric("Matches sportifs", len(football))
    col3.metric("Données économiques", len(economy))


# Cultural Events Section
elif section == "Événements culturels":
    st.title("🎫 Événements culturels")
    st.write("Analyse des événements.")
    # Ajouter les graphiques et visualisations pour les événements culturels ici.

    st.markdown("### Analyse des événements")
    if not event.empty:
        fig_event = px.histogram(event, x="city", color="country", title="Nombre d'événements par ville")
        st.plotly_chart(fig_event)

# Sports Data Section
elif section == "Données sportives":
    st.title("🏆 Données sportives")
    st.write("Analyse des performances sportives.")
    # Ajouter les graphiques et visualisations pour les données sportives ici.

    st.markdown("### Performances des équipes")
    if not football.empty:
        football["date"] = pd.to_datetime(football["date"])
        fig_scores = px.line(
            football, x="date", y="status", color="competition",
            title="Tendance des performances sportives"
        )
        st.plotly_chart(fig_scores)

    st.markdown("### Comparaison des compétitions")
    fig_competitions = px.bar(
        football, x="competition", color="competition",
        title="Nombre de matches par compétition"
    )
    st.plotly_chart(fig_competitions)

# Economic Indicators Section
elif section == "Indicateurs économiques":
    st.title("📊 Indicateurs économiques")
    st.write("Analyse des données économiques.")
    # Ajouter les graphiques et visualisations pour les indicateurs économiques ici.

    st.markdown("### Analyse temporelle")
    if not economy.empty:
        economy["date"] = pd.to_datetime(economy["date"])
        fig_economy = px.line(
            economy, x="date", y="value", color="indicator",
            title="Évolution des indicateurs économiques"
        )
        st.plotly_chart(fig_economy)

    st.markdown("### Distribution des indicateurs")
    fig_dist = px.box(economy, x="indicator", y="value", color="indicator")
    st.plotly_chart(fig_dist)

elif section == "Analyse avancée":
    st.title("🔍 Analyse avancée")
    st.write("Analyse approfondie des données.")

    st.markdown("### Corrélation entre les variables")
    if not economy.empty:
        # Sélectionner uniquement les colonnes numériques
        numeric_cols = economy.select_dtypes(include=[float, int])
        corr_matrix = numeric_cols.corr()
        fig_corr = px.imshow(
            corr_matrix,
            title="Matrice de corrélation des indicateurs économiques",
            labels=dict(color="Corrélation"),
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            color_continuous_scale='RdBu_r',
            zmin=-1, zmax=1
        )
        st.plotly_chart(fig_corr)

    st.markdown("### Analyse de régression")
    if not economy.empty:
        fig_regression = px.scatter(
            economy, x="date", y="value", color="indicator",
            trendline="ols",  # Ajout de la ligne de tendance
            title="Analyse de régression des indicateurs économiques"
        )
        st.plotly_chart(fig_regression)















from datetime import datetime

current_year = datetime.now().year

footer = f"""
<style>
footer {{
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #2E2E2E;
    text-align: center;
    padding: 2px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin: 0;
}}
footer a {{
    color: #4CAF50;
    text-decoration: none;
    margin: 0 5px;
    font-size: 24px;
}}
footer a:hover {{
    text-decoration: underline;
}}
footer p {{
    margin: 5px;
    font-size: 14px; 
}}
footer .copyright {{
    font-size: 12px;
    color: #888;
}}
</style>
<footer>
    <p>
        <a href="https://www.linkedin.com/in/hamady-gackou-687216251" target="_blank">
            <i class="fa fa-linkedin"></i>
        </a>
        <a href="https://github.com/gackouhamady" target="_blank">
            <i class="fa fa-github"></i>
        </a>
    </p>
    <p class="copyright">&copy; {current_year} Hamady Gackou</p>
</footer>
"""

# Affichage du footer
st.markdown(footer, unsafe_allow_html=True)
