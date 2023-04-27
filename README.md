# Regression_App
Brief sur la regression linéaire.


# Application de prédiction de prix des voitures

Ce code utilise Streamlit pour créer une interface utilisateur permettant à l'utilisateur de saisir les caractéristiques d'une voiture et d'obtenir une prédiction de son prix à l'aide d'un modèle pré-entrainé.

Le modèle utilisé est chargé à partir du fichier 'Price_Reg_Model.joblib' en utilisant la bibliothèque joblib.

Les caractéristiques de la voiture peuvent être saisies dans différents champs tels que l'état de la route, le type de carburant, le nombre de portes, le type de véhicule, etc.

Une fois que l'utilisateur a entré toutes les caractéristiques, elles sont stockées dans un dataframe pandas et utilisées pour effectuer une prédiction de prix en utilisant le modèle pré-entrainé. Le résultat est ensuite affiché à l'utilisateur.

L'interface utilisateur comprend également une image montrant la courbe d'apprentissage du modèle.

# FastAPI

Le fichier Fast.py permet d'utiliser fastAPI pour rendre le modele accecible pour des requetes API.

# Ydata

Un fichier html Ydata.html est disponible afin d'avoir un aperçu globale du DataSet.

# Utils

Vous y trouverez tout les étapes du travail effectué a commencé par le nettoyage du DataSet dans le fichier netoyage.ipynb jusqu'au déploiement avec Streamlit et FastAPI.

# Précisions

Plusieurs images sont disponibles afin de rendre le contenu du DataSet comprehensible pour ceux a qui les voitures sa parle pas trop.

