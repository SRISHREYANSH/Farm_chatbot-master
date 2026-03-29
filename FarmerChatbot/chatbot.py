import json
import random
import pickle
from nltk.tokenize import word_tokenize

# Load trained model
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load intents file
with open("intents.json", "r") as file:
    data = json.load(file)

def get_response(user_input):
    tokens = word_tokenize(user_input.lower())
    query = " ".join(tokens)
    intent = model.predict([query])[0]

    for i in data["intents"]:
        if i["tag"] == intent:
            return random.choice(i["responses"])
    
    return "Sorry, I didn't understand that."

# Test chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", get_response(user_input))
