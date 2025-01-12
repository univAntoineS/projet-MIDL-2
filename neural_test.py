import pandas as pd
import numpy as np
from tensorflow import keras

from module.separateData import *


X_train = pd.read_csv("data/X_train_reg.csv", index_col=0)
Y_train = pd.read_csv("data/Y_train.csv" ,index_col = 0)

X_test = pd.read_csv("data/X_test_reg.csv", index_col=0)
Y_test = pd.read_csv("data/Y_test.csv" ,index_col = 0)

# _,_,Y_train = sep(X_train,Y_train)
# _,_,Y_test = sep(X_test,Y_test)

X_train,Y_train,_ = sep(X_train,Y_train)
X_test,Y_test,_ = sep(X_test,Y_test)

model = keras.models.load_model("nn/checkpoint.model.keras")


model.evaluate(x=X_train, y=Y_train)
model.evaluate(x=X_test, y=Y_test)





