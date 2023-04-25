import streamlit as st
import joblib
from Regress import preprocessor

# Charger le modèle
model = joblib.load('Price_Reg_Model.joblib')




# Définir l'interface utilisateur avec Streamlit
st.title('Application de prédiction de prix des voitures')


new_car ={
    "car_ID": [1],
    
    "etat_de_route": [3],
    
    "carburant": ["gas"],
    
    "turbo": ["standard"],
    
    "nombre_portes": [2],
    
    "type_vehicule": ["decapotable"],
    
    "roues_motrices": ["arriere"],
    
    "emplacement_moteur": ["devant"],
    
    "empattement": [2.25],
    
    "longueur_voiture": [4.29],
    
    "largeur_voiture": [1.63],
    
    "hauteur_voiture": [1.24],
    
    "poids_vehicule": [1.27],
    
    "type_moteur": ["ACT"],
    
    
    "nombre_cylindres": [4],
    
    "taille_moteur": [34904],
    "systeme_carburant": ["carburateur 2 corps"],
    "taux_alésage": [3.47],
    "course": [2.68],
    "taux_compression": [9],
    "chevaux": [111],
    "tour_moteur": [5000],
    "consommation_ville": [21],
    "consommation_autoroute": [27],
    "marque": ["audi"],
    "modele": ["fox"],
    
}


# Créer les champs pour les entrées utilisateur
car_ID = 1

etat_de_route = st.selectbox('Etat de route', [-3,-2,-1,0,1,2,3])
carburant = st.selectbox('Carburant',['gas','diesel'])
turbo = st.selectbox('Turbo',['turbo','standard'])
nombre_portes = st.selectbox('Nombre Portes',[2,4])
type_vehicule = st.selectbox('Type Vehicule',['decapotable', 'hayon', 'berline', 'break', 'coupe'])
roues_motrices = st.selectbox('Roues Motrices',['arriere', 'avant', '4motrice'])
emplacement_moteur = st.selectbox('Emplacement Moteur',['devant', 'derrier'])
empattement = st.number_input('Empattement en metres', min_value=0, max_value=40)
longueur_voiture = st.number_input('Longuer en metres', min_value=0, max_value=40)
largeur_voiture = st.number_input('Largeur en metres', min_value=0, max_value=40)
hauteur_voiture = st.number_input('Hauteur en metres', min_value=0, max_value=40)
poids_vehicule = st.number_input('Poids en tonnes', min_value=0, max_value=50)
type_moteur = st.selectbox('Type de Moteur',[
        'double ACT', 
        'soupapes en tête à manchon', 
        'ACT',
        'ligne des cylindres', 'moteur rotatif',
        'soupapes en tête à flux croisés', 'double ACT à soupapes en V'] )
nombre_cylindres = st.selectbox('Nombre de cylindres',[ 2,3,4,5,6,8,12])
taille_moteur = st.number_input('Taille moteur', min_value=0, max_value=500000)

year = st.number_input('Année de la voiture', min_value=1950, max_value=2023, step=1)
mileage = st.number_input('Kilométrage de la voiture', min_value=0, max_value=1000000, step=1000)
fuel_type = st.selectbox('Type de carburant', ['Essence', 'Diesel', 'GPL', 'Hybride', 'Electrique'])
transmission = st.selectbox('Type de transmission', ['Manuelle', 'Automatique'])
marque = st.selectbox('Marque de la voiture', ['Audi', 'BMW', 'Chevrolet', 'Dodge', 'Ford', 'Honda', 'Hyundai', 'Jeep', 'Kia', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Porsche', 'Subaru', 'Toyota', 'Volkswagen'])
modele = st.text_input('Modèle de la voiture')

# Préparer les entrées utilisateur pour la prédiction
user_inputs = [[car_ID, car_model, year, mileage, fuel_type, transmission]]

# Appliquer la transformation de prétraitement
prediction_inputs = preprocessor.transform(user_inputs)

# Effectuer la prédiction avec le modèle
prediction = model.predict(prediction_inputs)

# Afficher le résultat de la prédiction
st.write('Le prix prédit de cette voiture est:', prediction[0])


