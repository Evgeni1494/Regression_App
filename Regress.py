import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split,learning_curve
import matplotlib.pyplot as plt
import numpy as np

# Charger les données
df = pd.read_csv("voitures.csv")


# Séparer les features et la variable cible
X = df.drop(["prix"], axis=1)
y = df["prix"]

# Diviser les données en ensemble d'entraînement et ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Identifier les colonnes catégorielles et numériques
cat_cols = X.select_dtypes(include="object").columns.tolist()
num_cols = X.select_dtypes(include=["int", "float"]).columns.tolist()

# Créer les transformateurs pour les colonnes catégorielles et numériques
cat_transformer = Pipeline(steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))])
num_transformer = Pipeline(steps=[("scaler", StandardScaler()), ("poly", PolynomialFeatures(degree=2, include_bias=False))])

# Créer le ColumnTransformer pour appliquer les transformateurs aux colonnes correspondantes
preprocessor = ColumnTransformer(transformers=[("cat", cat_transformer, cat_cols), ("num", num_transformer, num_cols)])

# Créer le pipeline complet avec la régularisation Ridge
model = Pipeline(steps=[("preprocessor", preprocessor), ("regressor", Ridge(alpha=1.0))])

# Entraîner le pipeline sur l'ensemble d'entraînement
model.fit(X_train, y_train)

# Évaluer les performances du pipeline sur l'ensemble de test
score = model.score(X_test, y_test)
print("Score:", score)