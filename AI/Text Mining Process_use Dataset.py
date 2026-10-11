# Get a dataset and use NLP :

import pandas as pan
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

Dataset = pan.read_csv("San's  DataScience Folder/000 ds csv files/copy fake reviews dataset.csv")
# print(Dataset)

Labs = [
    "CG",
    "CG",
    "OR",
    "OR"
]

vector = CountVectorizer()
Trans = vector.fit_transform(Dataset)

MultiNB = MultinomialNB()
MultiNB.fit(Trans, Labs)

Test = ["Excellent quality product. Perfect for my ccozinha."]

T_Data = vector.transform(Test)
Predict = MultiNB.predict(T_Data)

print("Test line :", Test[0])
print("Predict   :", Predict[0])
print("Completed...")


