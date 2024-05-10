from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
sentiment_score = analyzer.polarity_scores("I love using NLTK for NLP!")
