import json
import random
import string
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    tokens = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    return ' '.join([lemmatizer.lemmatize(w) for w in tokens])

def train_bot_model(intent_file="intents.json"):
    with open(intent_file, "r") as f:
        data = json.load(f)

    X, y = [], []
    for intent in data['intents']:
        for pattern in intent['patterns']:
            X.append(clean_text(pattern))
            y.append(intent['tag'])

    model = make_pipeline(TfidfVectorizer(), LogisticRegression())
    model.fit(X, y)
    return model, data

def get_bot_response(model, data, user_input):
    cleaned = clean_text(user_input)
    tag = model.predict([cleaned])[0]
    
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses']), tag
    return "I'm not sure I understand.", "unknown"
