

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from nltk.chunk import RegexpParser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

Text = "A Dream Can Change your Life"
endc = ("=-=-"*23)
print(endc)
# 1___ORGINAL TEXT :
print("1. ORGINAL TEXT :---")
print(Text)
print(endc)


# 2___TEXT MINING USE NLP:
Token = word_tokenize(Text)
print("2. WORD EXTRACTION :---")
print(Token)
print(endc)

# 3___TOKENIZE :
print("3. TOKENIZE :---")
print(Token)
print(endc)

# 4___STEMMING :
print("4. STEMMING :---")
psr = PorterStemmer()
for Word in Token:
    print(Word, "==>", psr.stem(Word))
print(endc)

# 5___LEMMATIZATION :
print("5. LEMMATIZATION :---")
lem = WordNetLemmatizer()
for Word in Token:
    print(Word, "<==>", lem.lemmatize(Word))
print(endc)

# 6 ___PART OF SPEECH (POS) TAGGING :
print("6. POS TAG :---")
postg = pos_tag(Token)
for Word, Tag in postg:
    print(Word, "==", Tag)
print(endc)

# 7___SYNTAX ANALYSIS :
print("7. SYNTAX ANALYSIS :---")
Grammar = r"""
NP : {<DT>?<JJ>*<NN>}
"""
Reg_Pars = RegexpParser(Grammar)
New = Reg_Pars.parse(postg)
print(New)
print(endc)

# CHUNKING :
print("8. CHUNKING :---")
Chunk_Gram = r"""
NP : {<DT>?<JJ>*<NN>}
"""
chunk_pars = RegexpParser(Chunk_Gram)
ch_result = chunk_pars.parse(postg)
print(ch_result)
print(endc)


# 9___MACHINE LEARNING + NLP :
print("9. MACHINE LEARNING + NLP :---")

Docs = [
    "A Dream can change your life.",
    "A Dream Give Positive",
    "She is a Worst Girl."
]

Labs = [
    "Positive",
    "Positive",
    "Negative"
]

vector = CountVectorizer()
x = vector.fit_transform(Docs)

MultiNB = MultinomialNB()
MultiNB.fit(x, Labs)

Test = ["She is a Good Gril."]

T_Data = vector.transform(Test)
Prediction = MultiNB.predict(T_Data)

print("Test line  :", Test[0])
print("Prediction :", Prediction[0])
print("Test ===> Fully Completed >  *_*")