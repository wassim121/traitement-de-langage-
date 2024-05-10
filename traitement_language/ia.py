import pandas as pd
from textblob import TextBlob

# Charger les données
data = pd.read_csv("data.csv", sep=",")

# Nettoyer les données
data["texte"] = data["texte"].str.lower().str.replace("[^a-zA-Z0-9 ]", " ")

# Analyser le sentiment
data["sentiment"] = [TextBlob(text).sentiment.polarity for text in data["texte"]]

# Afficher les résultats
print(data)
