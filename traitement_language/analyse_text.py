import nltk

# Définir le texte
text = """
Ceci est un long texte que nous souhaitons résumer. Il contient plusieurs phrases et paragraphes. 
Le but est d'extraire les phrases les plus importantes pour créer un résumé concis et informatif.
"""

# Tokeniser le texte en phrases
sentences = nltk.sent_tokenize(text)

# Calculer le score de chaque phrase
scores = [nltk.TextRank(sentence).score() for sentence in sentences]

# Sélectionner les phrases avec les scores les plus élevés
top_sentences = sorted(sentences, key=lambda x: scores[x], reverse=True)[:2]

# Générer le résumé
resume = " ".join(top_sentences)

# Afficher le résumé
print(resume)
a