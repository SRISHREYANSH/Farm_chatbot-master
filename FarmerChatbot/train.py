print("Train.py script is running...")

import json
import pickle
import numpy as np
import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
print("Downloading NLTK resources...")
nltk.download("punkt")
print("Downloaded 'punkt'.")

nltk.download("wordnet")
print("Downloaded 'wordnet'.")

print("Converting text to numbers...")
if not patterns:
    raise ValueError("Error: 'patterns' list is empty. Check your intents.json file!")

X = vectorizer.fit_transform(patterns).toarray()
print("Vectorization complete.")



# Load training data
print("Loading intents.json...")
with open("intents.json", "r") as file:
    data = json.load(file)
print("intents.json loaded.")

lemmatizer = WordNetLemmatizer()
vectorizer = CountVectorizer()

# Preprocess the data
patterns = []
labels = []
classes = []


print("Processing training data...")
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words = [lemmatizer.lemmatize(w.lower()) for w in tokens]
        sentence = " ".join(words)
        patterns.append(sentence)
        labels.append(intent["tag"])

    if intent["tag"] not in classes:
        classes.append(intent["tag"])

print("Data processed. Converting to numerical format...")
X = vectorizer.fit_transform(patterns).toarray()
y = np.array([classes.index(label) for label in labels])

# Train a simple Naive Bayes model
print("Training model...")
model = MultinomialNB()
model.fit(X, y)
print("Model training complete.")

# Save the trained model and vectorizer
print("Saving model...")
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Training complete! Model saved as chatbot_model.pkl.")
