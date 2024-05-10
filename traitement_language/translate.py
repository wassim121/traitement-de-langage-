from googletrans import Translator

t1 = "je m'appelle wassim"
translator = Translator()

# Traduction du texte en anglais
translated_text = translator.translate(t1, dest='en')
print(translated_text.text)





from googletrans import Translator

t1 = "je m'appelle wassim"
translator = Translator()

# Détection de la langue du texte
detected_lang = translator.detect(t1)
print(detected_lang.lang)




from googletrans import Translator

t1 = "Les API de Google Cloud basées sur l'IA vous permettent de traduire des documents, des sites Web, des applications, des fichiers audio, des vidéos et plus encore à grande échelle, en bénéficiant d'une qualité exceptionnelle, ainsi que d'un niveau de contrôle et de sécurité pensé pour les entreprises"
translator = Translator()

# Traduction du texte en anglais en spécifiant la langue source (français)
translated_text = translator.translate(t1, src='fr', dest='en')
print(translated_text.text)



