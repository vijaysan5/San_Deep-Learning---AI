# _____Single :-----

import pandas as pan
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

"Read Dataset :--"
Data = pan.read_csv("D:\Sangavi A\San's  DataScience Folder\\000 ds csv files\Adult csv file.csv")

"Remove Missing Values :--"
Data = Data.replace("?", pan.NA)
Data = Data.dropna()

"Encode Categorical Columns :--"
len = LabelEncoder()
for clmn in Data.columns :
    if Data[clmn].dtype == "object" :
        Data[clmn] = len.fit_transform(Data[clmn])

"Features and Target :--"
ab = Data.drop("income", axis=1)
xy = Data["income"]

"Sclae Futures :--"
scl = StandardScaler()
ab = scl.fit_transform(ab)

"Split Data :---"
ab_train, ab_test, xy_train, xy_test = train_test_split(
    ab, xy, test_size=0.2, random_state=42
)

from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, classification_report

SLP = Perceptron(
    max_iter=1000,
    random_state=42
)

SLP.fit(ab_train, xy_train)

Predict = SLP.predict(ab_test)

print("<===== Single =====>")
print("Perceptron Accuracy :", accuracy_score(xy_test, Predict))
print("Classifer :\n", classification_report(xy_test, Predict))




print("=="*23)




# _____Multi :-----

import pandas as pan
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

"Read Dataset :---"
Data = pan.read_csv("D:\Sangavi A\San's  DataScience Folder\\000 ds csv files\Adult csv file.csv")

"Remove Missing Values :---"
Data = Data.replace("?", pan.NA)
Data = Data.dropna()

"Encode Categorical Columns :---"
len = LabelEncoder()
for clmn in Data.columns :
    if Data[clmn].dtype == "object" :
        Data[clmn] = len.fit_transform(Data[clmn])

"Futures and Target :---"
ab = Data.drop("income", axis=1)
xy = Data["income"]

"Sclae Features :---"
scl = StandardScaler()
ab = scl.fit_transform(ab)

"Split Data :---"
ab_train, ab_test, xy_train, xy_test = train_test_split(
    ab, xy, test_size=0.2, random_state=42
)

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

mlp = MLPClassifier(
    hidden_layer_sizes=(64,32),
    activation="relu",
    solver="adam",
    max_iter=500,
    random_state=42
)

mlp.fit(ab_train, xy_train)
Predict = mlp.predict(ab_test)

print("<===== Multi =====>")
print("MLP Accuracy :", accuracy_score(xy_test, Predict))
print("Classifer :\n", classification_report(xy_test, Predict))