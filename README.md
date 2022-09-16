# Projet House Prices de A à Z

## Fichier requirements pour l'environnement
- Pour conda: conda_requirements.txt
- Pour pip: requirements.txt

## Première étape récupération des données
- Scraping de seloger.com : scrap.py
- seloger-cleaned.csv

## Deuxième étape: nettoyage des données
- HousePricesAZ_preparationdesdonnees-OneHotEnconder.ipynb

## Troisième étape: entrainement d'un modèle xgboost
- HousePricesAZ_XGBoost.ipynb
- HousepricesAZ_modelXGBoost.ipynb
- houseprices_keras_model.ipynb

## Quatrième étape: affichage via l'API Web Flask
- app.py
- templates/
- static/

## Lancement de l'application
- python app.py