import pandas as pan
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

"Read Dataset :"
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

"Build Tensor Flow Model :---"
tf_model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

"Compile :---"
tf_model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)

tf_model.fit(ab_train, xy_train, epochs = 10, batch_size = 32)

"Evaluate :---"
loss, accuracy = tf_model.evaluate(ab_test, xy_test)

print("Accuracy :===>", accuracy)




# Tens :===>>><<<
import pandas as pan
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

ds = pan.read_csv("San's  DataScience Folder/000 ds csv files/Adult csv file.csv")

ds.columns = ds.columns.str.strip()

for clmn in ds.columns :
    if ds[clmn].dtype == "object" :
        ds[clmn] = ds[clmn].astype(str).str.strip()

"Replace and Remove Missing Values :"
Data = ds.replace("?", pan.NA)
Data = ds.dropna()

print("Data's Shape", ds.shape)


"Find Target Columns :"
possible_t = [
    "income",
    "Income",
    "salary",
    "Salary",
    "amount",
    "Amount"
]

Tgt = None
for clmn in possible_t:
    if clmn in ds.columns:
        Tgt = clmn
        break

if Tgt is None:
    Tgt = ds.columns[-1]

print("Target clmn:---", Tgt)  # output ===> income


# Encoding Dataset's Columns:===<
for clmn in ds.columns:
    if ds[clmn].dtype == "object" :
        len = LabelEncoder()
        ds[clmn] = len.fit_transform(ds[clmn])

# Features and Label===<
ax = ds.drop(Tgt, axis=1)
ay = ds[Tgt]

# Scaling Data:===<
scl = StandardScaler()
ax = scl.fit_transform(ax)

# Train Test Split :===<
ax_train, ax_test, ay_train, ay_test = train_test_split(
    ax,
    ay,
    test_size= 0.2,
    random_state= 42
)

# converting to Tensorflow :===<><><>===
ax_train = tf.constant(ax_train, dtype=tf.float32)
ax_test = tf.constant(ax_test, dtype=tf.float32)

ay_train = tf.constant(ay_train.values.reshape(-1,1), dtype=tf.float32)
ay_test = tf.constant(ay_test.values.reshape(-1,1), dtype=tf.float32)

# Variables Creating :
inputNote = ax_train.shape[1]

W_1 = tf.Variable(tf.random.normal([inputNote, 64]))
brd_1 = tf.Variable(tf.zeros([64]))

W_2 = tf.Variable(tf.random.normal([64,32]))
brd_2 = tf.Variable(tf.zeros([32]))

W_3 = tf.Variable(tf.random.normal([32,1]))
brd_3 = tf.Variable(tf.zeros([1]))

Optimizer = tf.optimizers.Adam(0.001)


# Forward Function:===<>
def forward(ax):
    hig1 = tf.nn.relu(tf.matmul(ax, W_1)+brd_1)
    hig2 = tf.nn.relu(tf.matmul(hig1, W_2)+brd_2)
    out = tf.sigmoid(tf.matmul(hig2, W_3)+brd_3)
    return out

# Training :===
epochs = 23

for epoch in range(epochs):
    with tf.GradientTape() as tape:
        prediction = forward(ax_train)

        loss = tf.reduce_mean(
            tf.keras.losses.binary_crossentropy(ay_train, prediction))

    Variable = [W_1, brd_1, W_2, brd_2, W_3, brd_3]
    Gradient = tape.gradient (loss, Variable)
    Optimizer.apply_gradients(zip(Gradient, Variable))
    Predict = tf.cast(prediction > 0.5, tf.float32)

    acq = tf.reduce_mean(
        tf.cast(tf.equal(Predict, ay_train), tf.float32)
    )

    print(f"Epcoh===>{epoch+1:02d} Loss===>{loss.numpy():.4f} Accuracy===>{acq.numpy()*100:.2f}%")


# Testing :===
prediction = forward(ax_test)
Predict = tf.cast(prediction > 0.5, tf.float32)
test_acq = tf.reduce_mean(
    tf.cast(tf.equal(Predict, ay_test), tf.float32)
)

print("\n\nTest Accuracy :", round(test_acq.numpy()*100,2), "%")


# Predict First 5 Records:===<><><>
print("\nPredictions")

Return = forward(ax_test[:5])

for a,b in enumerate(Return):
    if b.numpy()[0] > 0.5:
        print("Person", a+1, ": Income >50K")
    else:
        print("Person", a+1, ": Income <=50K")