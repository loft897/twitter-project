# Contexte 📇
Fondé en 2006, Twitter est aujourd'hui l'un des plus grands réseaux sociaux du monde. Avec plus de 100 millions d'utilisateurs et 340 millions de tweets postés par jour, la société a connu une croissance extrêmement rapide au fil des années.

Ce qui fait la particularité de Twitter, c'est les 140 caractères par tweet. Cela permet aux gens de partager leur opinion de manière très concise, créant des données vraiment intéressantes à analyser.

Un des cas d'utilisation courants est de réaliser une analyse de sentiment sur ces tweets pour analyser l'opinion publique sur un sujet donné. C'est votre mission.

# Objectifs du projet 🎯
Votre objectif en tant qu'équipe d'ingénieurs en apprentissage automatique est de :

Récupérer des flux de tweets en temps réel
Les utiliser pour analyser tous les tweets
Effectuer une analyse automatique des sentiments

# Où obtenir les données
Pour réaliser ce projet, vous devrez accéder à des données! Voici deux sources de données que vous pouvez utiliser :

Streamer des tweets en temps réel (NOTE: Il s'agit plus d'un tutoriel sur l'API que des données réelles) : https://developer.twitter.com/en/docs/tutorials/stream-tweets-in-real-time

IMPORTANT: Vous devrez créer un compte développeur Twitter et créer une application avant de pouvoir utiliser l'API.

# Livraisons 📬
Pour compléter ce projet, vous devrez produire :

Un schéma de l'infrastructure que vous avez choisi de construire et pourquoi vous l'avez construite de cette façon
Cela peut être dans un document Powerpoint ou Word.
Le code source de tous les éléments nécessaires à la construction de votre infrastructure
Une vidéo de votre infrastructure fonctionnelle sur un exemple
Vous pouvez utiliser Vidyard pour cela
Conseils 🦮
Pour vous aider dans votre tâche, nous aimerions vous donner quelques conseils sur la façon de mener ce projet.

# Comment puis-je construire l'algorithme?
Pour construire votre algorithme, vous pouvez utiliser n'importe quelle bibliothèque (sklearn, tensorflow), des API ou même des outils sans code.

Si vous ne voulez pas construire l'algorithme vous-même, n'hésitez pas à utiliser AmazonML, qui est un excellent outil API.
NB: N'oubliez pas de construire quelque chose qui est réutilisable ! Surtout en termes de prétraitement, utiliser un algorithme ne consiste pas seulement à utiliser un .predict()

# Je ne sais pas par où commencer
Tout d'abord, dans ce projet, vous devez au moins :

Entraîner un algorithme
Mettre en production
Stocker des données en temps réel dans une base de données

Voici notre recommandation sur où commencer :

Construire l'algorithme (lire à partir du CSV de la source de données -> prétraiter les données -> entraîner le modèle)
Loger le modèle avec Ml flow (stocker le modèle dans le serveur ml flow -> utiliser ce modèle directement à partir de mlflow -> ou construire une API)
Utiliser le modèle sur les données du consommateur kafka, stocker les données à partir d'un topic kafka (producteur de données en temps réel)
Stocker les données avec les prédictions dans un entrepôt de données
Tirer parti des données (Zapier, Tableau public, Airtbale), utilisez des outils sans code pour construire un moteur de notifications, visualiser les données ou plus.

# IMPORTANT
L'exemple ci-dessus n'est qu'une suggestion, vous pouvez dévier de cette infrastructure. Les seuls éléments minimaux que nous devons avoir sont :

Un élément qui collecte et stocke les données
Un élément qui consomme les données
Un processus ETL (ou ELT)

# Comment répartir le travail entre mes coéquipiers?
Travailler ensemble est la clé ici ! Vous pouvez diviser votre travail de plusieurs façons, mais voici une suggestion :

Un membre de l'équipe peut entraîner l'algorithme
Un membre de l'équipe peut construire l'infrastructure MLflow
Un membre de l'équipe peut créer le pipeline d'ingestion de données en temps réel

# Marche à suivre pour livrer le projet 1:
Créez un compte développeur Twitter :
Allez sur le site de Twitter Developer et suivez les instructions pour créer un compte développeur. Vous aurez besoin de ce compte pour accéder à l'API de Twitter et récupérer les tweets en temps réel.

Récupération des tweets en temps réel :
Une fois que vous avez accès à l'API de Twitter, utilisez-la pour commencer à récupérer des tweets en temps réel. Il existe de nombreuses bibliothèques et tutoriels en ligne qui peuvent vous aider à le faire en Python, comme Tweepy.

Prétraitement des données :
Les tweets que vous récupérez auront probablement besoin d'être prétraités avant de pouvoir être utilisés pour l'entraînement d'un modèle. Cela peut impliquer le nettoyage du texte, la suppression des stop words, la tokenisation, etc. Vous pouvez utiliser une bibliothèque comme NLTK pour cela.

Entraînement de l'algorithme :
Ensuite, vous devrez choisir un modèle pour votre analyse de sentiment. Vous pouvez commencer par un modèle simple comme une régression logistique ou un Naive Bayes, ou utiliser un modèle plus complexe comme un réseau de neurones. Vous aurez également besoin d'un ensemble de données d'entraînement pour cette étape. Vous pouvez trouver de nombreux ensembles de données d'analyse de sentiment en ligne, ou vous pouvez étiqueter un petit ensemble de tweets vous-même.

Utilisation de MLflow :
MLflow est une plateforme open source pour gérer le cycle de vie du Machine Learning. Vous pouvez l'utiliser pour suivre vos expériences, enregistrer et comparer les modèles et les déployer. Consultez la documentation de MLflow pour savoir comment l'utiliser.

Mise en place d'un pipeline Kafka :
Kafka est une plateforme de streaming distribuée qui permet de publier et de s'abonner à des flux de données en temps réel. Vous pouvez l'utiliser pour consommer les tweets que vous récupérez de l'API Twitter et les passer à votre modèle pour obtenir des prédictions. Vous aurez besoin d'installer Kafka et de configurer un producteur et un consommateur.

Stocker les données dans un entrepôt de données :
Vous pouvez utiliser un système de base de données comme PostgreSQL pour stocker vos tweets et leurs scores de sentiment correspondants. Vous devrez configurer une base de données et écrire du code pour insérer les données dans la base de données.

Visualisation des données :
Enfin, vous pouvez utiliser un outil comme Tableau pour visualiser vos données. Vous pouvez créer un tableau de bord qui montre, par exemple, le sentiment moyen par jour, le nombre de tweets positifs et négatifs, etc.

# Marche à suivre pour livrer le projet 2:

Construire l'algorithme : Commencez par lire des données à partir d'un CSV ou d'une autre source de données. Vous devrez ensuite prétraiter ces données pour les rendre utilisables pour l'entraînement d'un modèle. Enfin, entraînez le modèle à l'aide d'une bibliothèque comme sklearn ou tensorflow.

Loger le modèle avec MLflow : Une fois votre modèle entraîné, vous devrez le stocker dans un serveur MLflow. Vous pouvez ensuite utiliser ce modèle directement à partir de MLflow, ou créer une API pour y accéder.

Utiliser le modèle sur les données du consommateur Kafka : Vous devrez créer un consommateur Kafka qui lira les données en temps réel à partir d'un sujet Kafka. Ces données peuvent ensuite être passées à votre modèle pour obtenir des prédictions.

Stocker les données avec les prédictions dans un entrepôt de données : Les prédictions de votre modèle, ainsi que les données d'origine, doivent être stockées dans un entrepôt de données pour une analyse ultérieure.

Tirer parti des données : Enfin, vous pouvez utiliser des outils sans code comme Zapier, Tableau Public ou Airtable pour construire un moteur de notifications, visualiser les données ou faire plus.

Documenter l'infrastructure : Vous devez également créer un schéma de l'infrastructure que vous avez construite, expliquant pourquoi vous l'avez construite de cette façon. Cela peut être fait dans un document Powerpoint ou Word.

Créer une vidéo de démonstration : Enfin, créez une vidéo de votre infrastructure en action à l'aide d'un outil comme Vidyard.

N'oubliez pas que ce ne sont que des directives. Vous pouvez choisir de suivre une approche différente si vous le souhaitez. L'important est de respecter les objectifs du projet.