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
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hello", "Hi", "Hey", "Good morning", "Good evening"],
            "responses": ["Hello!", "Hi there!", "Welcome!"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "Goodbye", "See you", "Take care", "See you later"],
            "responses": ["Goodbye!", "See you again!", "Take care!"]
        },
        {
            "tag": "name",
            "patterns": ["What is your name?", "Who are you?", "Tell me your name"],
            "responses": ["I am an ANN chatbot.", "My name is AI chatbot."]
        },
        {
            "tag": "thanks",
            "patterns": ["Thank you", "Thanks", "Thanks a lot", "Thank you so much"],
            "responses": ["You're welcome!", "Happy to help!", "My pleasure!"]
        },
        {
            "tag": "help",
            "patterns": ["Can you help me?", "I need help", "Please help me", "Help me"],
            "responses": ["Sure! How can I help you?", "Of course! Tell me your problem."]
        },
        {
            "tag": "study",
            "patterns": ["I want to study", "Help me with studies", "How to study well?", "Study tips"],
            "responses": ["Make a daily study timetable.", "Study regularly and practice daily!"]
        },
        {
            "tag": "weather",
            "patterns": ["How is the weather?", "Is it raining?", "Tell me about weather", "Is it sunny today?"],
            "responses": ["I cannot check live weather.", "Please check a weather app for current updates."]
        },
        {
            "tag": "food",
            "patterns": ["What is your favourite food?", "I am hungry", "Suggest some food", "I want to eat"],
            "responses": ["I like pizza!", "You can try biryani.", "Have something delicious!"]
        },
        {
            "tag": "time",
            "patterns": ["What time is it?", "Tell me the time", "Current time", "Can you check the time?"],
            "responses": ["Please check your device for the current time.", "I hope you are having a good day!"]
        },
        {
            "tag": "motivation",
            "patterns": ["Motivate me", "I feel sad", "I am tired", "Give me motivation", "I feel depressed"],
            "responses": ["Believe in yourself!", "Never give up. Keep trying!", "Every day is a new opportunity."]
        }
    ]
}
