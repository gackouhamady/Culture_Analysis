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
    football = football.rename(columns={"dates": "date"})
    economy = economy.rename(columns={"dates": "date"})
    
    return event, football, economy

event, football, economy = load_data()


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
    st.title("📊 Rapport du Projet ")
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
        options=["Économie vs Événements", "Économie vs Football", "Événements vs Football", "Football, Économie et Événements"]
    )

    # ---------------------------- Économie vs Événements ----------------------------
    if option == "Économie vs Événements":
        st.markdown("### Impact des Événements Culturels sur l'Économie")

        if 'events' in locals() and len(events) > 0:
            events['dates'] = pd.to_datetime(event['dates'])  # Assurer que les dates des événements sont au format DateTime

            # Fusionner les données des événements avec les données économiques sur la base des dates
            econ_with_events = economy.merge(event[['dates', 'city']], left_on='date', right_on='dates', how='left')

            fig_event_impact = px.scatter(
                econ_with_events, 
                x="dates", 
                y="value", 
                color="city",
                title="Impact des événements culturels sur les indicateurs économiques"
            )
            st.plotly_chart(fig_event_impact)

    # ---------------------------- Économie vs Football ----------------------------
    elif option == "Économie vs Football":
        st.markdown("### Impact des Performances Sportives sur l'Économie")

       # Assuming 'economy' and 'football' DataFrames are already defined

        # Filtrage des données de football pour l'analyse des performances
        if 'football' in locals() and len(football) > 0:
            football['date'] = pd.to_datetime(football['date'])  # Assurer que les dates sont au format DateTime

            # Calculer l'impact des résultats des matchs sur le PIB (ici basé sur la performance de l'équipe)
            football["economic_impact"] = football.apply(lambda x: 1 if x["performance_home_team"] == "winner" else -1, axis=1)

            # Convertir la colonne 'date' dans le DataFrame 'economy' au format datetime
            economy['date'] = pd.to_datetime(economy['date'])


            # Localiser les colonnes 'date' au fuseau horaire UTC
            economy['date'] = economy['date'].dt.tz_localize('UTC', ambiguous='NaT', nonexistent='shift_forward')
 
            # Convertir les colonnes 'date' au même fuseau horaire
            economy['date'] = economy['date'].dt.tz_convert('UTC')
            football['date'] = football['date'].dt.tz_convert('UTC')

            # Agréger les données économiques en fonction des performances sportives (impact positif ou négatif)
            econ_with_football = economy.merge(football[['date', 'economic_impact']], on='date', how='left')

            fig_impact = px.line(
                econ_with_football, 
                x="date", 
                y="value", 
                color="economic_impact", 
                title="Impact des résultats sportifs sur les indicateurs économiques"
            )
            st.plotly_chart(fig_impact)

    # ---------------------------- Événements vs Football ----------------------------
    elif option == "Événements vs Football":
        st.markdown("### Interaction entre les événements culturels et les performances sportives")

        if 'football' in locals() and len(football) > 0 and 'events' in locals() and len(events) > 0:
            # Fusionner les données des événements avec les données de football
            events['dates'] = pd.to_datetime(events['dates'])
            football['date'] = pd.to_datetime(football['date'])

            events_with_football = events.merge(football[['date', 'home_team', 'away_team']], left_on='dates', right_on='date', how='left')

            fig_event_football_impact = px.scatter(
                events_with_football,
                x="dates",
                y="home_team",  # Exemple d'affichage d'une équipe à domicile par rapport à la date de l'événement
                color="away_team",
                title="Interaction entre événements culturels et performances sportives"
            )
            st.plotly_chart(fig_event_football_impact)

    # ---------------------------- Football, Économie et Événements ----------------------------
    elif option == "Football, Économie et Événements":
        st.markdown("### Interaction combinée entre Événements, Football et Économie")

        if 'football' in locals() and len(football) > 0 and 'events' in locals() and len(events) > 0 and not economy.empty:
            # Fusionner les trois ensembles de données (football, événements, économie)
            events['dates'] = pd.to_datetime(events['dates'])
            football['date'] = pd.to_datetime(football['date'])

            # Fusionner les événements et le football sur les dates
            events_with_football = events.merge(football[['date', 'home_team', 'away_team']], left_on='dates', right_on='date', how='left')

            # Fusionner le résultat final avec les données économiques
            final_data = events_with_football.merge(economy[['date', 'value']], left_on='dates', right_on='date', how='left')

            fig_combined_impact = px.line(
                final_data,
                x="dates",
                y="value",  # Indicateur économique
                color="home_team",  # Par exemple, en fonction de l'équipe à domicile
                line_dash="away_team",  # Utiliser l'équipe à l'extérieur comme ligne de séparation
                title="Interaction combinée entre Événements, Football et Indicateurs Économiques"
            )
            st.plotly_chart(fig_combined_impact)

    # ---------------------------- Prévisions économiques basées sur les événements à venir ----------------------------

    st.markdown("### Prévisions économiques basées sur les événements futurs")
    if not economy.empty:
        # Filtrer les données économiques
        
        economy = economy.dropna(subset=['value'])  # Supprimer les lignes avec des valeurs manquantes
        economy = economy[np.isfinite(economy['value'])]  # Garder seulement les valeurs finies

        economy['date'] = pd.to_datetime(economy['date'])
        economy['date_ordinal'] = economy['date'].apply(lambda x: x.toordinal())  # Convertir les dates en valeurs ordinales

        # Préparer les données pour la régression
        X = economy[['date_ordinal']]  # Données indépendantes (dates)
        y = economy['value']  # Valeurs à prédire

                # Vérifier et nettoyer les données
        if economy['value'].isnull().any() or not np.isfinite(economy['value']).all():
            raise ValueError("Les données contiennent des valeurs manquantes ou infinies.")
        

        # Normaliser les valeurs du PIB
        scaler = StandardScaler()
        y_normalized = scaler.fit_transform(y.values.reshape(-1, 1))

        # Entraîner le modèle de régression linéaire
        model = LinearRegression()
        model.fit(X, y_normalized)

        # Prédire les valeurs futures (par exemple, pour les 3 prochaines années)
        future_dates = pd.date_range(start=economy['date'].max(), periods=12, freq='M')  # Prédire sur 12 mois
        future_dates_ordinal = future_dates.map(lambda x: x.toordinal()).values.reshape(-1, 1)
        predictions_normalized = model.predict(future_dates_ordinal)

        # Inverser la normalisation pour obtenir les valeurs prédictives originales
        predictions = scaler.inverse_transform(predictions_normalized)

        # Affichage des prévisions
        prediction_df = pd.DataFrame({
            'Date': future_dates,
            'Prédiction du PIB': predictions.flatten()
        })

        fig_forecast = px.line(
            prediction_df, 
            x='Date', 
            y='Prédiction du PIB', 
            title="Prévisions économiques basées sur les événements à venir"
        )
        st.plotly_chart(fig_forecast)

    # ---------------------------- Synthèse et Interaction des Données ----------------------------

    st.markdown("### Synthèse des Interactions entre Événements, Sport et Économie")

    st.write("Analyse complète de l'interaction entre l'économie, les événements culturels et sportifs.")
    st.write("Cette analyse permet de visualiser l'impact cumulé de ces trois domaines sur les indicateurs économiques.")
















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
