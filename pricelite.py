import streamlit as st
import joblib
import pandas as pd
# Charger le modèle
model = joblib.load('Price_Reg_Model.joblib')




# Définir l'interface utilisateur avec Streamlit
st.title('Application de prédiction de prix des voitures')


# Créer les champs pour les entrées utilisateur
car_ID = 1

etat_de_route = st.selectbox('Etat de route', [3,2,1,0,-1,-2,-3])
carburant = st.selectbox('Carburant',['gas','diesel'])
turbo = st.selectbox('Turbo',['turbo','standard'])
nombre_portes = st.selectbox('Nombre Portes',[2,4])
type_vehicule = st.selectbox('Type Vehicule',['decapotable', 'hayon', 'berline', 'break', 'coupe'])
roues_motrices = st.selectbox('Roues Motrices',['arriere', 'avant', '4motrice'])
emplacement_moteur = st.selectbox('Emplacement Moteur',['devant', 'derrier'])
empattement = st.number_input('Empattement en metres', min_value=0.0, max_value=400.0,step=0.01)
longueur_voiture = st.number_input('Longuer en metres', min_value=0.0, max_value=400.0,step=0.01)
largeur_voiture = st.number_input('Largeur en metres', min_value=0.0, max_value=400.0,step=0.01)
hauteur_voiture = st.number_input('Hauteur en metres', min_value=0.0, max_value=400.0,step=0.01)
poids_vehicule = st.number_input('Poids en tonnes', min_value=0.0, max_value=500.0,step=0.01)
type_moteur = st.selectbox('Type de Moteur',[
        'double ACT', 
        'soupapes en tête à manchon', 
        'ACT',
        'ligne des cylindres', 'moteur rotatif',
        'soupapes en tête à flux croisés', 'double ACT à soupapes en V'] )
nombre_cylindres = st.selectbox('Nombre de cylindres',[ 2,3,4,5,6,8,12])
taille_moteur = st.number_input('Taille moteur', min_value=0.0, max_value=500000.0,step=0.01)
systeme_carburant = st.selectbox('Systeme carburant', 
                                 ['injection multipoint multipoint port unique',
                                'carburateur 2 corps', 'injection carburant multipoint',
                                'carburateur 1 corps', 'injection monopoint',
                                'carburateur 4 corps', 'injection indirecte',
                                'injection D monopoint'])
taux_alésage = st.number_input('Taux alésage', min_value=0.0, max_value=20.0,step=0.01)
course = st.number_input('Course', min_value=0.0, max_value=20.0,step=0.01)
taux_compression = st.number_input('Taux compression', min_value=0.0, max_value=40.0,step=0.01)
chevaux = st.number_input('Puissance en chevaux',min_value=0.0, max_value=2000.0,step=0.01)
tour_moteur = st.number_input('Tours moteur',min_value=0.0, max_value=10000.0,step=0.01)
consommation_ville = st.number_input('Consomation en ville',min_value=0.0, max_value=10000.0,step=0.01)
consommation_autoroute = st.number_input('Consomation en autoroute',min_value=0.0, max_value=10000.0,step=0.01)
marque = st.selectbox('Marque de la voiture', 
                      ['alfa-romeo', 'audi', 
                    'bmw', 'chevrolet', 'dodge', 'honda',
                    'isuzu', 'jaguar', 'mazda', 'buick', 'mercury', 'mitsubishi',
                    'nissan', 'peugeot', 'plymouth', 'porsche', 'renault', 'saab',
                    'subaru', 'toyota', 'volkswagen', 'volvo'])
modele = st.text_input('Modèle de la voiture')

# Préparer les entrées utilisateur pour la prédiction
# user_inputs = [[car_ID, 
#                 etat_de_route, 
#                 carburant, turbo, 
#                 nombre_portes, 
#                 type_vehicule,
#                 roues_motrices,
#                 emplacement_moteur,
#                 empattement,
#                 longueur_voiture,
#                 largeur_voiture,
#                 hauteur_voiture,
#                 poids_vehicule,
#                 type_moteur,
#                 nombre_cylindres,
#                 taille_moteur,
#                 systeme_carburant,
#                 taux_alésage,
#                 course,
#                 taux_compression,
#                 chevaux,
#                 tour_moteur,
#                 consommation_ville,
#                 consommation_autoroute,
#                 marque,
#                 modele,
#                 ]]

user_inputs = pd.DataFrame(data ={
    "car_ID":car_ID, 
                "etat_de_route" : etat_de_route, 
                "carburant" : carburant, 
                "turbo" : turbo, 
                "nombre_portes" : nombre_portes, 
                "type_vehicule" : type_vehicule,
                "roues_motrices" : roues_motrices,
                "emplacement_moteur" : emplacement_moteur,
                "empattement" : empattement,
                "longueur_voiture" : longueur_voiture,
                "largeur_voiture" : largeur_voiture,
                "hauteur_voiture" : hauteur_voiture,
                "poids_vehicule" : poids_vehicule,
                "type_moteur" : type_moteur,
                "nombre_cylindres" : nombre_cylindres,
                "taille_moteur" : taille_moteur,
                "systeme_carburant" : systeme_carburant,
                "taux_alésage" : taux_alésage,
                "course" : course,
                "taux_compression" : taux_compression,
                "chevaux" : chevaux,
                "tour_moteur" : tour_moteur,
                "consommation_ville" : consommation_ville,
                "consommation_autoroute" : consommation_autoroute,
                "marque" : marque,
                "modele" : modele
                }, index=[0])

if st.button("Predire"):
    user_inputs = pd.DataFrame(data ={
    "car_ID":car_ID, 
                "etat_de_route" : etat_de_route, 
                "carburant" : carburant, 
                "turbo" : turbo, 
                "nombre_portes" : nombre_portes, 
                "type_vehicule" : type_vehicule,
                "roues_motrices" : roues_motrices,
                "emplacement_moteur" : emplacement_moteur,
                "empattement" : empattement,
                "longueur_voiture" : longueur_voiture,
                "largeur_voiture" : largeur_voiture,
                "hauteur_voiture" : hauteur_voiture,
                "poids_vehicule" : poids_vehicule,
                "type_moteur" : type_moteur,
                "nombre_cylindres" : nombre_cylindres,
                "taille_moteur" : taille_moteur,
                "systeme_carburant" : systeme_carburant,
                "taux_alésage" : taux_alésage,
                "course" : course,
                "taux_compression" : taux_compression,
                "chevaux" : chevaux,
                "tour_moteur" : tour_moteur,
                "consommation_ville" : consommation_ville,
                "consommation_autoroute" : consommation_autoroute,
                "marque" : marque,
                "modele" : modele
                }, index=[0])
    prediction = model.predict(user_inputs)
    st.markdown("<h3 style='text-align: center;'>Le prix prédit de cette voiture est: {:.0f} $</h3>".format(prediction[0]), unsafe_allow_html=True)


# Afficher le résultat de la prédiction



