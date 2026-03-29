from flask import Flask, request, jsonify
import pickle
import json
import random
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Load model and data
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("intents.json", "r") as file:
    data = json.load(file)

@app.route("/chat", methods=["POST"])
def chatbot():
    user_input = request.json.get("message")
    tokens = word_tokenize(user_input.lower())
    query = " ".join(tokens)
    intent = model.predict([query])[0]

    for i in data["intents"]:
        if i["tag"] == intent:
            response = random.choice(i["responses"])
            return jsonify({"response": response})
    
    return jsonify({"response": "Sorry, I didn't understand that."})

if __name__ == "_main_":
    app.run(debug=True)