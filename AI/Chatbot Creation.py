import numpy as np
import random
import nltk
import json

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import squantial
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

lemmatizer = WordNetLemmatizer()

Texts = {
    "intents" : [
        {
            "tag" : "greetings",
            "patterns" : ["Hi", "Hay", "Hlo"],
            "response" : ["Hey", "Hi there!", "Hello!"]
        },
        {
            "tag" : "thank",
            "patterns" : ["Thanks", "Thank You"],
            "response" : ["You Are Welcome"]
        },
        {
            "tag" : "help",
            "patterns" : ["help me", "please help"],
            "response" : ["How can I Help you ?", "Yes, I can Help You."]
        },
    ]
}