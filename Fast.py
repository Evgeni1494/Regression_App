import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
# Charger le modèle
model = joblib.load('Price_Reg_Model.joblib')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Créer une classe de modèle de requête Pydantic
class CarPriceRequest(BaseModel):
    car_ID =1
    etat_de_route: int
    carburant: str
    turbo: str
    nombre_portes: int
    type_vehicule: str
    roues_motrices: str
    emplacement_moteur: str
    empattement: float
    longueur_voiture: float
    largeur_voiture: float
    hauteur_voiture: float
    poids_vehicule: float
    type_moteur: str
    nombre_cylindres: int
    taille_moteur: float
    systeme_carburant: str
    taux_alésage: float
    course: float
    taux_compression: float
    chevaux: float
    tour_moteur: float
    consommation_ville: float
    consommation_autoroute: float
    marque: str
    modele: str




# Définir une route API
@app.post("/predict_price")
def predict_price(car: CarPriceRequest):
    # Transformer les données d'entrée de l'utilisateur en DF
    input_data = pd.DataFrame(data ={"car_ID":car.car_ID,
                                     "etat_de_route":car.etat_de_route, 
                                     "carburant":car.carburant, 
                                     "turbo":car.turbo, 
                                     "nombre_portes":car.nombre_portes, 
                                     "type_vehicule":car.type_vehicule, 
                                     "roues_motrices":car.roues_motrices, 
                                     "emplacement_moteur":car.emplacement_moteur, 
                                     "empattement":car.empattement, 
                                     "longueur_voiture":car.longueur_voiture, 
                                     "largeur_voiture":car.largeur_voiture, 
                                     "hauteur_voiture":car.hauteur_voiture, 
                                     "poids_vehicule":car.poids_vehicule, 
                                     "type_moteur":car.type_moteur, 
                                     "nombre_cylindres":car.nombre_cylindres, 
                                     "taille_moteur":car.taille_moteur, 
                                     "systeme_carburant":car.systeme_carburant, 
                                     "taux_alésage":car.taux_alésage, 
                                     "course":car.course, 
                                     "taux_compression":car.taux_compression, 
                                     "chevaux":car.chevaux, 
                                     "tour_moteur":car.tour_moteur, 
                                     "consommation_ville":car.consommation_ville, 
                                     "consommation_autoroute":car.consommation_autoroute, 
                                     "marque":car.marque,
                                     "modele":car.modele},index=[0])
    # Faire la prédiction
    prediction = model.predict(input_data)
    # Retourner la prédiction
    return {"prediction": prediction[0]}
