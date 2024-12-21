## Problématique
Comment pouvons-nous concevoir un tableau de bord temps réel intégrant des données sur les événements culturels (concerts et festivals), les performances sportives (football) et les indicateurs économiques, afin d'analyser l’interaction entre l’activité humaine, l’économie et le sport dans une zone géographique donnée ?

## Importance du sujet
Ce projet vise à démontrer comment des données disparates, mais interdépendantes, peuvent être collectées, analysées et visualisées en temps réel pour révéler des insights significatifs. Dans un monde où les décisions économiques, sociales et organisationnelles s’appuient de plus en plus sur des données actualisées, ce tableau de bord fournit un outil unique pour comprendre l’impact économique et social des événements culturels et sportifs.

## Objectifs concrets
1. **Centraliser et analyser des données multi-sources** : Événements musicaux, performances sportives, et indicateurs économiques à partir de différentes API en temps réel.  
2. **Mettre en évidence les interactions potentielles** : Par exemple, l’impact des événements culturels et sportifs sur les indicateurs économiques locaux, ou l’influence des performances sportives sur la popularité des équipes et leurs régions.  
3. **Développer un outil d’aide à la décision** : Un tableau de bord visuel et interactif permettant de suivre et de prévoir les tendances, utile pour les gestionnaires d’événements, les économistes ou les autorités locales.  
4. **Démontrer la faisabilité technique** : Validation du concept avec des scripts d’automatisation et une analyse périodique résumée dans MongoDB, tout en garantissant la pertinence et l’actualité des données affichées.

## Exploration de la base de données MongoDB

Pour explorer la base de données, il faut télécharger MongoDB Compass et se connecter à la base avec ce lien :  
`mongodb+srv://<db_username>:<db_password>@cluster0.1lwk5.mongodb.net/`

- **db_username** : `user`  
- **db_password** : `user`


## Cron Job

- 0 */3 * * * /path/vers/crontab.sh


## Configuration et Tests de Scripts Python avec PyMongo et Tâches Cron
- Pour tout problème lié à PyMongo, vous pouvez créer directement un environnement virtuel Python. Dans cet environnement, vous pourrez tester les scripts Python, définir la tâches cron ...  ci  dessus :  (0 */3 * * * /path/vers/crontab.sh)
