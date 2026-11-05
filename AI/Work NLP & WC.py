import pandas as pan
import matplotlib.pyplot as mplt
import nltk
import string
from wordcloud import wordcloud
from nltk.corpus import stopwords

Dataset = pan.read_csv("San's  DataScience Folder/000 ds csv files/TestReviews.csv")
print("===== >>> Read <<< =====")

def word(text):
    text = text.lower()
    text = text.translate(str.)
