## Problématique
Comment pouvons-nous concevoir un tableau de bord temps réel intégrant des données sur les événements culturels, les performances sportives (football) et les indicateurs économiques, afin d'analyser l’interaction entre l’activité humaine, l’économie et le sport dans une zone géographique donnée ?

## Importance du sujet
Ce projet vise à démontrer comment des données disparates, mais interdépendantes, peuvent être collectées, analysées et visualisées en temps réel pour révéler des insights significatifs. Dans un monde où les décisions économiques, sociales et organisationnelles s’appuient de plus en plus sur des données actualisées, ce tableau de bord fournit un outil unique pour comprendre l’impact économique et social des événements culturels et sportifs.

## Objectifs concrets
1. **Centraliser et analyser des données multi-sources** : Événements, performances sportives, et indicateurs économiques à partir de différentes API en temps réel.  
2. **Mettre en évidence les interactions potentielles** : Par exemple, l’impact des événements culturels et sportifs sur les indicateurs économiques locaux, ou l’influence des performances sportives sur la popularité des équipes et leurs régions.  
3. **Développer un outil d’aide à la décision** : Un tableau de bord visuel et interactif permettant de suivre et de prévoir les tendances, utile pour les gestionnaires d’événements, les économistes ou les autorités locales.  
4. **Démontrer la faisabilité technique** : Validation du concept avec des scripts d’automatisation et une analyse périodique résumée dans MongoDB, tout en garantissant la pertinence et l’actualité des données affichées.


# API utilisées

## 1. **Ticketmaster API**
   - **Nature** : Temps réel
   - **Contenu des données** : Cette API fournit des informations sur les événements (concerts, festivals, événements sportifs, etc.), telles que :
     - Nom de l'événement
     - Date et heure de l'événement
     - Lieu (salle, stade, etc.)
     - Ville et pays
     - Catégorie d'événement (musique, sport, théâtre, etc.)
     - Informations sur les billets , prix
   - **Périodicité** : Les données sont mises à jour en temps réel, selon la disponibilité des événements et des informations mises à jour par Ticketmaster.
   - **Moyen d’accès aux données** :
     - **API** : Les données sont accessibles via une API RESTful.
     - **Clé API** : Une clé d’API est nécessaire pour l'accès aux données. Cette clé peut être obtenue en s'inscrivant sur le site de Ticketmaster.
   - **Droit de réutilisation des données** :
     - **Conditions d'utilisation** : Les données sont protégées par des droits d’auteur et soumises aux conditions d'utilisation de Ticketmaster. L'utilisation des données est généralement limitée aux applications non commerciales. Pour toute utilisation commerciale (comme la revente ou la diffusion de données à des fins commerciales), une autorisation préalable de Ticketmaster est requise.
     - **Restrictions** : La réutilisation des données pour des projets commerciaux nécessite un accord spécifique avec Ticketmaster.

## 2. **Football Data API**
   - **Nature** : Temps réel
   - **Contenu des données** : Cette API fournit des données sur les compétitions de football à travers le monde. Les informations incluent :
     - Détails sur les compétitions (nom de la compétition, pays, saison)
     - Résultats des matchs
     - Classements des équipes
     - Statistiques de match (score, possession, tirs, etc.)
   - **Périodicité** : Les données sont mises à jour en temps réel ou très proche du temps réel pendant les matchs. Les résultats des matchs sont ajoutés dès qu'ils sont disponibles.
   - **Moyen d’accès aux données** :
     - **API** : L'accès aux données se fait via une API RESTful.
     - **Clé API** : Une clé API est nécessaire pour authentifier les requêtes. Elle peut être obtenue après inscription sur le site officiel de Football Data.
   - **Droit de réutilisation des données** :
     - **Conditions d'utilisation** : Les données sont fournies sous des conditions d'utilisation spécifiques. En général, les données peuvent être utilisées à des fins personnelles ou académiques. Pour un usage commercial (par exemple, pour une application de paris ou une plateforme commerciale), une licence spécifique est requise.
     - **Restrictions** : L’utilisation des données est limitée dans un cadre non commercial, sauf si un accord commercial est obtenu avec les propriétaires des données.

## 3. **World Bank API**
   - **Nature** : Pas en temps réel (données économiques historiques)
   - **Contenu des données** : Cette API fournit des données économiques détaillées pour différents pays, notamment :
     - PIB par pays (en dollars constants ou courants)
     - Indicateurs économiques comme la population, la croissance économique, les investissements, etc.
     - Données sur la pauvreté, l'accès à l'éducation, la santé, les infrastructures, etc.
     - Ces données couvrent plusieurs décennies, avec des mises à jour périodiques.
   - **Périodicité** : Les données économiques sont mises à jour annuellement ou selon la publication de nouveaux rapports économiques par la Banque Mondiale.
     - Les ensembles de données peuvent couvrir des périodes comme 2013-2022, selon l'indicateur spécifique.
   - **Moyen d’accès aux données** :
     - **API** : L'accès aux données se fait via une API RESTful, sans nécessiter d'authentification.
     - **Téléchargement** : Les données peuvent également être téléchargées en format JSON ou XML pour une utilisation hors ligne.
     - **Token nécessaire** : Aucun token n'est nécessaire pour accéder aux données de l'API.
   - **Droit de réutilisation des données** :
     - **Conditions d'utilisation** : Les données sont ouvertes au public et peuvent être utilisées gratuitement, sous réserve de respect des conditions d'utilisation de la Banque Mondiale. L’attribution est obligatoire si les données sont utilisées dans des publications ou des projets.
     - **Restrictions** : Les données peuvent être utilisées librement dans des projets académiques, de recherche ou d'analyse. Pour un usage commercial, il est recommandé de vérifier les conditions spécifiques sur le site de la Banque Mondiale.














## Exploration de la base de données MongoDB

Pour explorer la base de données, il faut télécharger MongoDB Compass et se connecter à la base avec ce lien :  
`mongodb+srv://<db_username>:<db_password>@cluster0.1lwk5.mongodb.net/`

- **db_username** : `user`  
- **db_password** : `user`


## Cron Job

- 0 */3 * * * /path/vers/crontab.sh


## Configuration et Tests de Scripts Python avec PyMongo et Tâches Cron
- Pour tout problème lié à PyMongo, vous pouvez créer directement un environnement virtuel Python. Dans cet environnement, vous pourrez tester les scripts Python, définir la tâches cron ...  ci  dessus :  (0 */3 * * * /path/vers/crontab.sh)
