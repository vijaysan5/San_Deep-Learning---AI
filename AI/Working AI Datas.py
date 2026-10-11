import pandas as pan
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

"Read Dataset :---"
Bank = pan.read_csv("San's  DataScience Folder/000 ds csv files/bank-data.csv")

Bank = Bank.replace("?", pan.NA)
Bank = Bank.dropna()

len = LabelEncoder()
for bk in Bank.columns:
    if Bank[bk].dtype == "object" :
        Bank[bk] = len.fit_transform(Bank[bk])

ab = Bank.drop("income", axis = 1)
xy = Bank["income"]

ss = StandardScaler()
ab = ss.fit_transform(ab)


abItest, abItrain, xyItest, xyItrain = train_test_split(
    ab, xy, test_size=0.2, random_state=42
)

tf_mdl = tf.keras.Sequential([
    tf.keras.layers.Dense(64, "relu"),
    tf.keras.layers.Dense(32, "relu"),
    tf.keras.layers.Dense(1, "sigmoid")
])

tf_mdl.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)

tf_mdl.fit(abItrain, xyItrain, epochs=10, batch_size = 32)

loss, accuracy = tf_mdl.evaluate(abItest,xyItest)

print("Accuracy :", accuracy)