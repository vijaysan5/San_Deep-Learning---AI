import os
import numpy as num
import matplotlib.pyplot as mplt
import seaborn as sb
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix

#  01._____DATA PATH :
DATASET = r"D:\Sangavi A\San's  DataScience Folder\Deep Learning Folder\AI - cnn\dataset"

DATA_TRAIN = os.path.join(DATASET, "train_f")
DATA_TEST = os.path.join(DATASET, "test_f")


#  02._____PARAMETERS :
S_IMAGE = 224
S_BATCH = 32
EPOCHS = 30


#  03._____DATA AUGMENTATION + TRAIN/VALIDATION SPLIT :
train_DataGen = ImageDataGenerator(
    rescale = 1.0/255,
    validation_split = 0.2,

    rotation_range = 20,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode = "nearest" 
)

train_Gen = train_DataGen.flow_from_directory(
    DATA_TRAIN,
    target_size = (S_IMAGE, S_IMAGE),
    batch_size = S_BATCH,
    class_mode = "categorical",
    subset = "training",
    shuffle = True
)

train_valid = train_DataGen.flow_from_directory(
    DATA_TRAIN,
    target_size = (S_IMAGE, S_IMAGE),
    batch_size = S_BATCH,
    class_mode = "categorical",
    subset = "validation",
    shuffle = False
)


#  04._____DATA TEST :
test_DataGen = ImageDataGenerator(
    rescale = 1.0/255
)

test_Gen = test_DataGen.flow_from_directory(
    DATA_TEST,
    target_size = (S_IMAGE, S_IMAGE),
    batch_size = S_BATCH,
    class_mode = "categorical",
    shuffle = False
)

#  05._____CHECH CLASSES :
Class_Name = list(train_Gen.class_indices.keys())

print("___CLASS___")

for a, name in enumerate(Class_Name):
    print(a ,":", name)

Num_Class = len(Class_Name)

print("\nNumber of Classes :", Num_Class)
print("Training Image :", train_Gen.samples)
print("Validation Image :", train_Gen.samples)
print("Test Image :", test_Gen.samples)


# 06._____BUILD CNN MODEL :
Model = models.Sequential([

    # Input :
    layers.Input(shape = (S_IMAGE, S_IMAGE, 3)),

    # CNN >>> B-ONE :
    layers.Conv2D(32, (3,3), activation = "relu"),
    layers.MaxPooling2D((2,2)),

    # CNN >>> B-TWO :
    layers.Conv2D(64, (3,3), activation = "relu"),
    layers.MaxPooling2D((2,2)),

    # CNN >>> B-THREE :
    layers.Conv2D(128, (3,3), activation = "relu"),
    layers.MaxPooling2D((2,2)),

    # CNN >>> B-FOUR :
    layers.Conv2D(256, (3,3), activation = "relu"),
    layers.MaxPooling2D((2,2)),

    # REGULARIZATION :
    layers.Dropout(0.5),

    # FLATTEN :
    layers.Flatten(),

    # CONNECTED LAYERS :
    layers.Dense(256, activation = "relu"),
    layers.Dropout(0.5),

    # OUTPUT :
    layers.Dense(Num_Class, activation = "softmax")
])


#  07._____MODEL SUMMARY :
Model.summary()


#  08._____COMPILE MODEL :
Model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate = 0.0001),
    loss = "categorical_crossentropy",
    metrics = ["accuracy"]
)


#  09._____CALL BACK :
CallBack = [
    tf.keras.callbacks.EarlyStopping(
        monitor = "val_loss",
        patience = 7,
        restore_best_weights = True
    ),

    tf.keras.callbacks.ReduceLROnPlateau(
        monitor = "val_loss",
        factor = 0.5,
        patience = 3,
        min_lr = 1e-7
    ),

    tf.keras.callbacks.ModelCheckpoint(
        "best_fruit_cnn.keras",
        monitor = "val_accuracy",
        save_best_only = True
    )
]


#  10._____TRAIN CNN :
TrainHist = Model.fit(
    train_Gen,
    validation_data = train_valid,
    epochs = EPOCHS,
    callbacks = CallBack
)


#  11._____TEST ACCURACY :
Test_Loss, Test_Accuracy = model.evaluate(test_Gen)

print("\nTest Loss :", Test_Loss)
print("Test Accuracy :", Test_Accuracy)


#  12._____TRAINING ACCURACY AND VALIDATION ACCURACY GRAPH :
mplt.figure(figsize = (10,5))
mplt.plot(
    TrainHist.history["accuracy"],
    label = "Training Accuracy"
)

mplt.plot(
    TrainHist.history["val_accuracy"],
    label = "Validation Accuracy"
)

mplt.title("==CNN Taining and Validation Accuracy==")
mplt.xlabel("--Epochs--")
mplt.ylabel("--Accuracy--")
mplt.legend()
mplt.grid()

mplt.show()


#  13._____TAINING LOSS AND VALIDATION LOSS GRAPH :
mplt.figure(figsize = (10,5))
mplt.plot(
    TrainHist.history["loss"],
    label = "Training Loss"
)

mplt.plot(
    TrainHist.history["val_loss"],
    label = "Validation Loss"
)

mplt.title("==CNN Training and Validation Loss==")
mplt.xlabel("--Epochs--")
mplt.ylabel("--Loss--")
mplt.legend()
mplt.grid()

mplt.show()


#  14._____PREDICTIONS :
test_Gen.reset()

Prediction = Model.predict(test_Gen)

PreClass = num.argmax(
    Prediction, axis = 1
)

TrueClass = test_Gen.classes


#   15._____CLASSIFICATION REPORT :

print ("\n===<>"*3)
print("\nClassification Report :\n")

print(
    classification_report(
        TrueClass,
        PreClass,
        target_names= Class_Name
    )
)


#  16._____CONFUSION MATRIX :
conf = confusion_matrix(
    TrueClass,
    PreClass
)

mplt.figure(figsize = (10,8))

sb.heatmap(
    annot = True,
    fmt = "d",
    xticklabels = Class_Name,
    yticklabels = Class_Name
)

mplt.title("==CNN Confusion Matrix==")
mplt.xlabel("--Prediction Class--")
mplt.ylabel("--True Class--")

mplt.show()


#  17._____SAVE THE MODEL :

Model.save("Fruit_Classification___CNN")
print("\n\n Fruit Classification is Saved.")