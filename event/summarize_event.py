import streamlit as st
import pandas as pd
import plotly.express as px
import pymongo
from datetime import datetime

from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Dashboard Intégré", page_icon="📊", layout="wide")

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
    football = pd.DataFrame(list(db["football_past_performance"].find()))
    economy = pd.DataFrame(list(db["economic_data"].find()))
    
    # Rename 'dates' column to 'date'
    event = event.rename(columns={"dates": "date"})
    football = football.rename(columns={"dates": "date"})
    economy = economy.rename(columns={"dates": "date"})
    
    return event, football, economy

event, football, economy = load_data()

# Function to safely convert date columns to datetime
def safe_to_datetime(df, column):
    try:
        # Filter out invalid dates before conversion
        df = df[df[column].apply(lambda x: pd.to_datetime(x, errors='coerce')).notnull()]
        df[column] = pd.to_datetime(df[column], errors='coerce')
    except Exception as e:
        st.error(f"Error converting {column} to datetime: {e}")
    return df

# Convert date columns to datetime safely
event = safe_to_datetime(event, "date")
football = safe_to_datetime(football, "date")
economy = safe_to_datetime(economy, "date")

# Sidebar navigation
# Sidebar avec des icônes spécifiques
with st.sidebar:
    section = option_menu(
        menu_title="Navigation",  # Titre du menu
        options=["Accueil", "Événements culturels", "Données sportives", "Indicateurs économiques"],  # Sections
        icons=["house", "music", "trophy", "bar-chart"],  # Icônes correspondantes
        menu_icon="list",  # Icône pour le menu global
        default_index=0,  # Section par défaut
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "blue", "font-size": "18px"},  # Couleur et taille des icônes
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},  # Couleur de sélection
        },
    )

# Sections
# Sections
section = "Accueil"
if section == "Accueil":
    st.title("🏠 Accueil")
    st.write("Bienvenue sur le tableau de bord intégré.")
    # Ajouter des contenus pour l'accueil ici.

    col1, col2, col3 = st.columns(3)
    col1.metric("Événements culturels", len(event))
    col2.metric("Matches sportifs", len(football))
    col3.metric("Données économiques", len(economy))

    st.markdown("#### Carte des événements")
    # Traitement des colonnes pour uniformiser les données
    events_df = event.rename(columns={"dates": "date", "name": "venue"})
    football_df = football.rename(columns={"home_team": "venue", "away_team": "opponent", "competition": "type"})

    # Ajouter des colonnes manquantes dans les deux DataFrames
    events_df["opponent"] = None
    events_df["type"] = "Event"
    
    # Handle placeholder dates and convert to datetime
    events_df["date"] = events_df["date"].apply(lambda x: None if x == '9999-09-09' else x)
    events_df["date"] = pd.to_datetime(events_df["date"], format='%Y-%m-%d', errors="coerce")

    football_df["city"] = None
    football_df["country"] = None
    football_df["opponent"] = football_df["opponent"]
    
    # Handle placeholder dates and convert to datetime
    football_df["date"] = football_df["date"].apply(lambda x: None if x == '9999-09-09' else x)
    football_df["date"] = pd.to_datetime(football_df["date"], format='%Y-%m-%d', errors="coerce")

    # Concaténer les deux DataFrames
    all_events = pd.concat([events_df, football_df], ignore_index=True)

    # Supprimer les lignes avec des dates invalides
    all_events = all_events.dropna(subset=["date"])

    # Carte des événements avec plotly
    st.markdown("#### Carte des événements")
    event_map = px.scatter_geo(
        all_events,
        locations="country",
        locationmode="country names",
        hover_name="venue",
        hover_data=["date", "type", "opponent"],
        title="Répartition des événements",
        color="type",
        size_max=15,
    )

    # Afficher la carte dans Streamlit
    st.plotly_chart(event_map)
# Cultural Events Section
elif section == "Événements culturels":
    st.title("🎵 Événements culturels")
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
        fig_economy = px.line(
            economy, x="date", y="value", color="indicator",
            title="Évolution des indicateurs économiques"
        )
        st.plotly_chart(fig_economy)

    st.markdown("### Distribution des indicateurs")
    fig_dist = px.box(economy, x="indicator", y="value", color="indicator")
    st.plotly_chart(fig_dist)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Développé par Hamady Gackou")