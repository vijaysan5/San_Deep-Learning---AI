import os
import numpy as num
import matplotlib.pyplot as mplt
import seaborn as sb
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix

#  01_____DATA PATH :
DATASET = r"D:\Sangavi A\San's  DataScience Folder\Deep Learning Folder\AI - cnn\dataset"

DATA_TRAIN = os.path.join(DATASET, "train_f")
DATA_TEST = os.path.join(DATASET, "test_f")


#  02_____PARAMETERS :
S_IMAGE = 224
S_BATCH = 32
EPOCHS = 30


#  03_____DATA AUGMENTATION + TRAIN/VALIDATION SPLIT :
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
    batch_size = S_batch,
    class_mode = "categorical",
    subset = "validation",
    shuffle = False
)


#  04_____DATA TEST :
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

#  05_____CHECH CLASSES :
Class_Name = list(train_Gen.class_indices.keys())

print("___CLASS___")

for a, name in enumerate(Class_Name):
    print(a ,":", name)

Num_Class = len(Class_Name)

print("\nNumber of Classes :", Num_Class)
print("Training Image :", train_Gen.samples)
print("Validation Image :", train_Gen.samples)
print("Test Image :", test_Gen.samples)

