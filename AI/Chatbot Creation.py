import numpy as np
import random
import nltk
import json

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
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


Words = []
Classes = []
Documents = []

# >>> Preprocessing <<< :
for intent in Texts["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern.lower())
        Words.extend(tokens)
        Documents.append((tokens, intent["tag"]))

        if intent["tag"] not in Classes:
            Classes.append(intent["tag"])

Words = [
    lemmatizer.lemmatize(w)
    for w in Words
    if w.isalnum()
]

Words = sorted(set(Words))
Classes = sorted(set(Classes))


# >>> Training <<< :
Train = []
for doc in Documents:
    pack = []

    sentence_words = [
        lemmatizer.lemmatize(w.lower())
        for w in doc[0]
    ]

    for word in Words:
        pack.append(1 if word in sentence_words else 0)

    Output = [0] * len(Classes)
    Output[Classes.index(doc[1])] = 1

    Train.append([pack, Output])

random.shuffle(Train)

ab = np.array([item[0] for item in Train])
xy = np.array([item[0] for item in Train])


# >>> ANN Model <<< :

model = Sequential()

model.add(Dense(128, input_shape=(len(X[0]),), activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(len(Classes), activation='softmax'))

# Compile model
model.compile(
    loss='categorical_crossentropy',
    optimizer=SGD(
        learning_rate=0.01,
        momentum=0.9,
        nesterov=True
    ),
    metrics=['accuracy']
)

# >>> Train chatbot <<<
model.fit(ab, xy, epochs=200, batch_size=5, verbose=1)


# >>> Chatbot Response Function <<<
def cbot_res(message):
    tokens = nltk.word_tokenize(message.lower())

    tokens = [
        lemmatizer.lemmatize(w)
        for w in tokens
        if w.isalnum()
    ]

    
