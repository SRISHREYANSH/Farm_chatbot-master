import json
import nltk
import random
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle

# Download necessary NLP tools
nltk.download('punkt')
nltk.download('stopwords')

# Load dataset
with open("intents.json", "r") as file:
    data = json.load(file)

stop_words = set(stopwords.words("english"))
X, y = [], []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = word_tokenize(pattern.lower())
        filtered = " ".join([word for word in tokens if word not in stop_words])
        X.append(filtered)
        y.append(intent["tag"])

# Train model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, y)

# Save model
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")
