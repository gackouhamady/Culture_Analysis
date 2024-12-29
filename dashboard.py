import streamlit as st
import pandas as pd
import plotly.express as px
import pymongo
from datetime import datetime
from dateutil import parser
from streamlit_option_menu import option_menu
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import plotly.graph_objects as go
import geopy
from geopy.geocoders import Nominatim
import numpy as np





 


# Set page configuration
st.set_page_config(page_title="Dashboard : Analyse Culturelle et Économique", page_icon="📊", layout="wide")


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
    football = football.rename(columns={"date": "date"})
    economy = economy.rename(columns={"dates": "date"})
    
    return event, football, economy

event, football, economy = load_data()


# Personnalisation du sidebar
with st.sidebar:
    section = option_menu(
        menu_title="Tableau de bord",  # Titre du menu
        options=["Rapport", "Accueil", "Événements culturels", "Données sportives", "Indicateurs économiques", "Analyse avancée"],  # Sections
        icons=["file", "house", "headphones", "trophy", "bar-chart", "graph-up"],  # Icônes correspondantes
        menu_icon="list",  # Icône pour le menu global
        default_index=0,  # Section par défaut
        styles={
            "container": {
                "padding": "5px", 
                "background-color": "#2E2E2E", 
                "height": "100%",  # Assure que la hauteur prend toute la fenêtre
                "display": "flex", 
                "flex-direction": "column", 
                "justify-content": "flex-start",  # Aligne les éléments au sommet de la sidebar
                "overflow": "auto"  # Permet de défiler si nécessaire
            },
            "icon": {
                "color": "blue", 
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "10px 10px", 
                "--hover-color": "#eee"
            },
            "nav-link-selected": {
                "background-color": "#02ab21"
            },
        }
    )




# Homepage
# Sections
if section == "Rapport":
    st.title("📊 Rapport du Projet ")
    st.markdown("### Sujet : Analyse et Visualisation des Données Multi-Sectorielles : Événements, Sports et Économie")
    st.markdown("**Auteur :** Hamady GACKOU")
    st.markdown("**Encadrant :** Francois-Xavier JOLLOIS, PhD  ")

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


# Streamlit UI

if section=="Accueil":
    st.title("🏠 Accueil")
    st.write("Bienvenue sur le tableau de bord intégré.")

    # Afficher les métriques
    col1, col2, col3 = st.columns(3)
    col1.metric("Événements culturels", len(event))
    col2.metric("Matches sportifs", len(football))
    col3.metric("Données économiques", len(economy))

    # Conversion en DataFrame
    event_df = pd.DataFrame(event)
    football_df = pd.DataFrame(football)
    economy_df = pd.DataFrame(economy)

    # ---------------------------------------------------------------------------------------------------
    # Affichage par tableaux avec filtres et métriques
    st.title("Tableaux des données")

    # Affichage des données des événements
    st.subheader("Événements culturels")
    st.dataframe(event_df)

    # Affichage des données des matchs
    st.subheader("Matches sportifs")
    st.dataframe(football_df)

    # Affichage des données économiques
    st.subheader("Données économiques")
    st.dataframe(economy_df)

    # ---------------------------------------------------------------------------------------------------
    # Graphiques interactifs pour visualiser les tendances
    st.title("Graphiques interactifs")

    # Conversion de la colonne '_id' en chaînes de caractères pour éviter les erreurs de sérialisation
    event_df['_id'] = event_df['_id'].astype(str)
    football_df['_id'] = football_df['_id'].astype(str)
    economy_df['_id'] = economy_df['_id'].astype(str)

    # Graphique des événements par pays
    event_count_by_country = event_df.groupby('country').size().reset_index(name='event_count')
    fig_event = px.bar(event_count_by_country, x='country', y='event_count', title='Événements culturels par pays')
    st.plotly_chart(fig_event)

    # Graphique des matchs par pays
    fig_football = px.bar(football_df, x='home_team', y='score_home_team', title='Scores des matchs par équipe à domicile')
    st.plotly_chart(fig_football)

    # Graphique des données économiques
    fig_economy = px.line(economy_df, x='country', y='value', title='Indicateurs économiques par pays')
    st.plotly_chart(fig_economy)
 
 

# Cultural Events Section
if section == "Événements culturels":
    st.title("🎫 Événements culturels")
    st.write("Analyse des événements.")

    st.markdown("### Analyse des événements")
    
    if not event.empty:
        # Analyse géographique
        fig_event_city = px.histogram(event, x="city", color="country", title="Nombre d'événements par ville")
        st.plotly_chart(fig_event_city)
        

         # 'classificationName' pour l'analyse des types d'événements
        fig_event_type = px.histogram(event, x="classificationName", title="Répartition des types d'événements")
        st.plotly_chart(fig_event_type)
        
        
        # Analyse des lieux
        fig_event_venue = px.histogram(event, x="venue", title="Nombre d'événements par lieu")
        st.plotly_chart(fig_event_venue)

# Sports Data Section
elif section == "Données sportives":
    st.title("🏆 Données sportives")
    st.write("Analyse des performances sportives.")
    # Ajouter les graphiques et visualisations pour les données sportives ici.

    st.markdown("### Performances des équipes")
    if not football.empty:
        football["date"] = pd.to_datetime(football["date"])
        
        # Tendance des performances sportives
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

    st.markdown("### Analyse des Scores")
    # Moyenne des Buts Marqués/Concédés
    football["goals"] = football["score_home_team"] + football["score_away_team"]
    avg_goals = football.groupby("competition")["goals"].mean().reset_index()
    fig_avg_goals = px.bar(
        avg_goals, x="competition", y="goals",
        title="Moyenne des Buts Marqués par Compétition",
        labels={"goals": "Moyenne des Buts"}
    )
    st.plotly_chart(fig_avg_goals)
    
    # Distribution des Scores
    fig_score_dist = px.histogram(
        football, x="goals",
        title="Distribution des Scores",
        labels={"goals": "Nombre de Buts"}
    )
    st.plotly_chart(fig_score_dist)

    st.markdown("### Analyse des Tendances Temporelles")
    # Performance au Fil du Temps
    fig_time_performance = px.line(
        football, x="date", y="score_home_team",
        title="Performance des Équipes au Fil du Temps",
        labels={"score_home_team": "Score à Domicile"}
    )
    st.plotly_chart(fig_time_performance)

   

    st.markdown("### Analyse des Joueurs")
    # Statistiques des Joueurs Clés
    player_stats = football.groupby("home_team")[["score_home_team", "score_away_team"]].sum().reset_index()
    fig_player_stats = px.bar(
        player_stats, x="home_team", y=["score_home_team", "score_away_team"],
        title="Statistiques des Joueurs Clés",
        labels={"value": "Nombre de Buts", "home_team": "Équipe"}
    )
    st.plotly_chart(fig_player_stats)

# Economic Indicators Section
elif section == "Indicateurs économiques":
    st.title("📊 Indicateurs économiques")
    st.write("Analyse des données économiques.")
    
    # Analyse Temporelle
    st.markdown("### Analyse Temporelle")
    if not economy.empty:
        economy["date"] = pd.to_datetime(economy["date"])
        fig_economy = px.line(
            economy, x="date", y="value", color="indicator",
            title="Évolution des indicateurs économiques"
        )
        st.plotly_chart(fig_economy)

    # Distribution des Indicateurs
    st.markdown("### Distribution des indicateurs")
    fig_dist = px.box(economy, x="indicator", y="value", color="indicator", 
                      title="Distribution des valeurs par indicateur")
    st.plotly_chart(fig_dist)

    # Analyse de la Croissance Économique
    st.markdown("### Croissance Économique Année par Année")
    economy["year"] = economy["date"].dt.year
    economy_grouped = economy.groupby(["year", "indicator"]).agg({"value": "sum"}).reset_index()
    economy_grouped["growth"] = economy_grouped.groupby("indicator")["value"].pct_change() * 100
    
    fig_growth = px.line(
        economy_grouped, x="year", y="growth", color="indicator", 
        title="Croissance économique annuelle"
    )
    st.plotly_chart(fig_growth)

    # Corrélation entre différents indicateurs économiques
    df = pd.DataFrame(economy)
    df['date'] = pd.to_datetime(df['date'], format='%Y').dt.year
    df_pivot = df.pivot_table(index='country', columns='date', values='value', aggfunc='first')
    corr_matrix = df_pivot.corr()

    st.markdown("### Corrélation entre les PIB des pays")
    fig_corr = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale='Viridis',
        colorbar=dict(title='Corrélation')
    ))

    fig_corr.update_layout(title="Matrice de Corrélation entre les PIB des pays en 2022")
    st.plotly_chart(fig_corr)

    # Détection des anomalies économiques (Isolation Forest)
    economy_pib = economy[economy['indicator'] == 'GDP (current US$)']

    # Normalisation des valeurs pour éviter que certaines valeurs ne dominent l'algorithme
    economy_scaled = economy_pib.copy()
    economy_scaled["value"] = StandardScaler().fit_transform(economy_scaled[["value"]])

    # Application de l'algorithme Isolation Forest pour détecter les anomalies
    isolation_forest = IsolationForest(contamination=0.05)  # Le taux d'anomalie (ici 5%)
    economy_scaled["anomaly"] = isolation_forest.fit_predict(economy_scaled[["value"]])

    # Visualisation des anomalies sur un graphique
    fig_anomalies = px.scatter(
        economy_scaled, 
        x="date", 
        y="value", 
        color="anomaly", 
        title="Détection des anomalies économiques (PIB)",
        labels={"anomaly": "Anomalie", "value": "PIB (en dollars US)"},
        color_continuous_scale='Viridis'
    )

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig_anomalies)

    # Prévision du PIB Futur (modèle ARIMA ou Holt-Winters)
    st.markdown("### Prévision des tendances économiques futures")
    economy_pib = economy[economy["indicator"] == "GDP (current US$)"]
    economy_pib = economy_pib[["date", "value"]].set_index("date")
    economy_pib = economy_pib.resample('A').sum()  # Agrégation par année

    model = ExponentialSmoothing(economy_pib["value"], trend="add", seasonal=None, damped_trend=True)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)  # Prévision pour les 5 prochaines années

    fig_forecast = go.Figure()
    fig_forecast.add_trace(go.Scatter(x=economy_pib.index, y=economy_pib["value"], mode='lines', name='Historique'))
    fig_forecast.add_trace(go.Scatter(x=forecast.index, y=forecast.values, mode='lines', name='Prévision', line=dict(dash='dot')))
    
    fig_forecast.update_layout(title="Prévision du PIB Futur (avec Holt-Winters)", xaxis_title="Année", yaxis_title="Valeur du PIB")
    st.plotly_chart(fig_forecast)

    # Analyse de la Variabilité des Indicateurs (Standard Deviation)
    economy_std_by_country = economy.groupby("country")["value"].std().reset_index()
    # Trier les pays en fonction de leur écart-type (de la plus grande variabilité à la plus petite)
    economy_std_by_country = economy_std_by_country.sort_values("value", ascending=False)

    # Affichage de la variabilité des PIB par pays
    st.markdown("### Variabilité des PIB par pays")
    fig_std = px.bar(economy_std_by_country, 
                    x="country", 
                    y="value", 
                    title="Variabilité des PIB des pays (écart-type) par pays",
                    labels={"value": "Écart-type du PIB (US$)", "country": "Pays"})

    st.plotly_chart(fig_std)
    
    
# Analyse Avancée 
elif section == "Analyse avancée":
    st.title("🔍 Analyse avancée")
    st.write("Analyse approfondie des données.")

    # ---------------------------- Sélection de l'option d'analyse ----------------------------
    option = st.selectbox(
        "Choisissez l'analyse à afficher:",
        options=["Prévision Économie et Événements", "Économie vs Football", "Événements vs Football", "Football, Économie et Événements"]
    )




    # ---------------------------- Économie vs Événements ----------------------------
    if option == "Prévision Économie et Événements":
        st.markdown("### Prévision des tendances économiques futures et événements passés et à venir")

        # Filtrage des données économiques (ici PIB)
        economy_pib = economy[economy["indicator"] == "GDP (current US$)"]
        economy_pib = economy_pib[["date", "value"]].set_index("date")
        economy_pib.index = pd.to_datetime(economy_pib.index)
        economy_pib = economy_pib.resample('A').sum()  # Agrégation par année

        # Modèle de prévision avec Holt-Winters
        model = ExponentialSmoothing(economy_pib["value"], trend="add", seasonal=None, damped_trend=True)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=5)  # Prévision pour les 5 prochaines années

        # Créer un graphique pour l'affichage des prévisions du PIB
        fig_forecast = go.Figure()
        fig_forecast.add_trace(go.Scatter(
            x=economy_pib.index,
            y=[value + (i * 0.05 * value) for i, value in enumerate(economy_pib["value"])],  # Écarter les points sur l'axe Y
            mode='lines', name='Historique'
        ))
        fig_forecast.add_trace(go.Scatter(
            x=forecast.index,
            y=[value + (i * 0.05 * value) for i, value in enumerate(forecast.values)],  # Écarter les points sur l'axe Y
            mode='lines', name='Prévision', line=dict(dash='dot')
        ))

        # Assurez-vous que la colonne 'date' est au format datetime
        event['date'] = pd.to_datetime(event['date'], errors='coerce')

        # Remplissez les dates manquantes avec une date future
        future_date = pd.to_datetime('2100-01-01')
        event['date'].fillna(future_date, inplace=True)

        # Filtrer les événements passés (avant la date actuelle)
        events_past = event[event['date'] < pd.to_datetime('today').normalize()]
        if len(events_past) > 0:
            fig_forecast.add_trace(go.Scatter(
                x=events_past['date'],
                y=[economy_pib['value'].mean() + (i * 0.05 * economy_pib['value'].mean()) for i in range(len(events_past))],  # Écarter les points sur l'axe Y
                mode='markers', name="Événements passés",
                marker=dict(color='blue', size=10, symbol='circle')
            ))

        # Filtrer les événements à venir (date actuelle ou ultérieure)
        events_upcoming = event[event['date'] >= pd.to_datetime('today').normalize()]
        if len(events_upcoming) > 0:
            fig_forecast.add_trace(go.Scatter(
                x=events_upcoming['date'],
                y=[forecast.mean() + (i * 0.05 * forecast.mean()) for i in range(len(events_upcoming))],  # Écarter les points sur l'axe Y
                mode='markers', name="Événements à venir",
                marker=dict(color='red', size=10, symbol='x')
            ))

        # Mise à jour du graphique pour inclure les titres et les axes
        fig_forecast.update_layout(
            title="Prévision du PIB Futur et Événements",
            xaxis_title="Année",
            yaxis_title="Valeur du PIB",
            showlegend=True
        )

        # Affichage du graphique dans Streamlit
        st.plotly_chart(fig_forecast)







    # ---------------------------- Économie vs Football ----------------------------
    elif option == "Économie vs Football":
        
            st.markdown("### Prévision des tendances économiques et analyse des interactions avec le sport")

            # Filtrage des données économiques (ici PIB)
            economy_pib = economy[economy["indicator"] == "GDP (current US$)"]
            economy_pib = economy_pib[["date", "value"]].set_index("date")
            economy_pib.index = pd.to_datetime(economy_pib.index)
            economy_pib = economy_pib.resample('A').sum()  # Agrégation par année

            # Modèle de prévision avec Holt-Winters
            model = ExponentialSmoothing(economy_pib["value"], trend="add", seasonal=None, damped_trend=True)
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=5)  # Prévision pour les 5 prochaines années

            # Créer un graphique pour l'affichage des prévisions du PIB
            fig_forecast = go.Figure()
            fig_forecast.add_trace(go.Scatter(
                x=economy_pib.index,
                y=[value + (i * 0.05 * value) for i, value in enumerate(economy_pib["value"])],  # Écarter les points sur l'axe Y
                mode='lines', name='Historique PIB'
            ))
            fig_forecast.add_trace(go.Scatter(
                x=forecast.index,
                y=[value + (i * 0.05 * value) for i, value in enumerate(forecast.values)],  # Écarter les points sur l'axe Y
                mode='lines', name='Prévision PIB', line=dict(dash='dot')
            ))


            # Conversion des colonnes de date en format datetime
            economy['date'] = pd.to_datetime(economy['date'])
            football['date'] = pd.to_datetime(football['date'], errors='coerce')  # Conversion des dates
            football['date'] = football['date'].dt.tz_localize(None)

            # Traitement des données de football
            football['date'] = pd.to_datetime(football['date'], errors='coerce')
            football_past = football[football['date'] < pd.to_datetime('today').normalize()]
            football_upcoming = football[football['date'] >= pd.to_datetime('today').normalize()]

            if len(football_past) > 0:
                fig_forecast.add_trace(go.Scatter(
                    x=football_past['date'],
                    y=[economy_pib['value'].mean() + (i * 0.05 * economy_pib['value'].mean()) for i in range(len(football_past))],  # Écarter les points sur l'axe Y
                    mode='markers', name="Matches passés",
                    marker=dict(color='green', size=10, symbol='circle')
                ))

            if len(football_upcoming) > 0:
                fig_forecast.add_trace(go.Scatter(
                    x=football_upcoming['date'],
                    y=[forecast.mean() + (i * 0.05 * forecast.mean()) for i in range(len(football_upcoming))],  # Écarter les points sur l'axe Y
                    mode='markers', name="Matches à venir",
                    marker=dict(color='orange', size=10, symbol='x')
                ))

            # Mise à jour du graphique pour inclure les titres et les axes
            fig_forecast.update_layout(
                title="Prévision du PIB, Matches de Football et Événements",
                xaxis_title="Date",
                yaxis_title="Valeur du PIB",
                showlegend=True
            )

            # Affichage du graphique dans Streamlit
            st.plotly_chart(fig_forecast)

    # ---------------------------- Événements vs Football ----------------------------
    elif option == "Événements vs Football":
        
        football['date'] = pd.to_datetime(football['date'], errors='coerce').dt.tz_localize(None)
        event['date'] = pd.to_datetime(event['date'], errors='coerce')

        # Filtrage des données par rapport à la date actuelle 
        
        
        football_past = football[football['date'] < pd.to_datetime('today').normalize()]
        football_upcoming = football[football['date'] >= pd.to_datetime('today').normalize()]

        event_past = event[event['date'] < pd.to_datetime('today').normalize()]
        event_upcoming = event[event['date'] >= pd.to_datetime('today').normalize()]

        # Création du graphique
        fig = go.Figure()

        # Ajout des événements passés de football
        
        
        if len(football_past) > 0:
            fig.add_trace(go.Scatter(
                x=football_past['date'],
                # Vérifier si 'economy_pib['value']' est une série ou un flottant

                 
                mode='markers',
                name="Matches passés",
                marker=dict(color='green', size=10, symbol='circle')
            ))

        # Ajout des événements futurs de football
        if len(football_upcoming) > 0:
            fig.add_trace(go.Scatter(
                x=football_upcoming['date'],
                y=[i for i in range(len(football_upcoming))],  # Positionner en fonction de l'indice
                mode='markers',
                name="Matches à venir",
                marker=dict(color='orange', size=10, symbol='x')
            ))

        # Ajout des événements culturels passés
        if len(event_past) > 0:
            fig.add_trace(go.Scatter(
                x=event_past['date'],
                y=[i for i in range(len(event_past))],  # Positionner en fonction de l'indice
                mode='markers',
                name="Événements culturels passés",
                marker=dict(color='blue', size=10, symbol='circle')
            ))

        # Ajout des événements culturels futurs
        if len(event_upcoming) > 0:
            fig.add_trace(go.Scatter(
                x=event_upcoming['date'],
                y=[i for i in range(len(event_upcoming))],  # Positionner en fonction de l'indice
                mode='markers',
                name="Événements culturels à venir",
                marker=dict(color='red', size=10, symbol='x')
            ))


        # Mise en page du graphique
        fig.update_layout(
            title="Distribution des événements culturels et sportifs",
            xaxis_title="Date",
            yaxis_title="Valeur indicatrice (écartée pour différenciation)",
            showlegend=True
        )

        # Affichage dans Streamlit
        st.markdown("### Analyse des interactions des événements culturels et sportifs")
        st.plotly_chart(fig)
        
   
   

    # ---------------------------- Football, Économie et Événements ----------------------------
    elif option == "Football, Économie et Événements":
            
            st.markdown("### Prévision des tendances économiques et analyse des interactions avec les événements culturels et sportifs")

            # Filtrage des données économiques (ici PIB)
            economy_pib = economy[economy["indicator"] == "GDP (current US$)"]
            economy_pib = economy_pib[["date", "value"]].set_index("date")
            economy_pib.index = pd.to_datetime(economy_pib.index)
            economy_pib = economy_pib.resample('A').sum()  # Agrégation par année

            # Modèle de prévision avec Holt-Winters
            model = ExponentialSmoothing(economy_pib["value"], trend="add", seasonal=None, damped_trend=True)
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=5)  # Prévision pour les 5 prochaines années

            # Créer un graphique pour l'affichage des prévisions du PIB
            fig_forecast = go.Figure()
            fig_forecast.add_trace(go.Scatter(
                x=economy_pib.index,
                y=[value + (i * 0.05 * value) for i, value in enumerate(economy_pib["value"])],  # Écarter les points sur l'axe Y
                mode='lines', name='Historique PIB'
            ))
            fig_forecast.add_trace(go.Scatter(
                x=forecast.index,
                y=[value + (i * 0.05 * value) for i, value in enumerate(forecast.values)],  # Écarter les points sur l'axe Y
                mode='lines', name='Prévision PIB', line=dict(dash='dot')
            ))


            # Conversion des colonnes de date en format datetime
            economy['date'] = pd.to_datetime(economy['date'])
            football['date'] = pd.to_datetime(football['date'], errors='coerce')  # Conversion des dates
            football['date'] = football['date'].dt.tz_localize(None)

            # Traitement des données de football
            football['date'] = pd.to_datetime(football['date'], errors='coerce')
            football_past = football[football['date'] < pd.to_datetime('today').normalize()]
            football_upcoming = football[football['date'] >= pd.to_datetime('today').normalize()]

            if len(football_past) > 0:
                fig_forecast.add_trace(go.Scatter(
                    x=football_past['date'],
                    y=[economy_pib['value'].mean() + (i * 0.05 * economy_pib['value'].mean()) for i in range(len(football_past))],  # Écarter les points sur l'axe Y
                    mode='markers', name="Matches passés",
                    marker=dict(color='green', size=10, symbol='circle')
                ))

            if len(football_upcoming) > 0:
                fig_forecast.add_trace(go.Scatter(
                    x=football_upcoming['date'],
                    y=[forecast.mean() + (i * 0.05 * forecast.mean()) for i in range(len(football_upcoming))],  # Écarter les points sur l'axe Y
                    mode='markers', name="Matches à venir",
                    marker=dict(color='orange', size=10, symbol='x')
                ))

            # Traitement des données d'événements culturels
            event['date'] = pd.to_datetime(event['date'], errors='coerce')
            event_past = event[event['date'] < pd.to_datetime('today').normalize()]
            event_upcoming = event[event['date'] >= pd.to_datetime('today').normalize()]

            if len(event_past) > 0:
                fig_forecast.add_trace(go.Scatter(
                    x=event_past['date'],
                    y=[economy_pib['value'].mean() + (i * 0.1 * economy_pib['value'].mean()) for i in range(len(event_past))],  # Écarter les points sur l'axe Y
                    mode='markers', name="Événements passés",
                    marker=dict(color='blue', size=10, symbol='circle')
                ))

            if len(event_upcoming) > 0:
                fig_forecast.add_trace(go.Scatter(
                    x=event_upcoming['date'],
                    y=[forecast.mean() + (i * 0.1 * forecast.mean()) for i in range(len(event_upcoming))],  # Écarter les points sur l'axe Y
                    mode='markers', name="Événements à venir",
                    marker=dict(color='red', size=10, symbol='x')
                ))

            # Mise à jour du graphique pour inclure les titres et les axes
            fig_forecast.update_layout(
                title="Prévision du PIB, Matches de Football et Événements",
                xaxis_title="Date",
                yaxis_title="Valeur du PIB",
                showlegend=True
            )

            # Affichage du graphique dans Streamlit
            st.plotly_chart(fig_forecast)


    # ---------------------------- Footer du  tableau  de bord ----------------------------


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
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="30" height="30">
        </a>
        <a href="https://github.com/gackouhamady" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="30" height="30">
        </a>
    </p>
    <p class="copyright">&copy; {current_year} Hamady Gackou</p>
</footer>
"""

# Affichage du footer
st.markdown(footer, unsafe_allow_html=True)
