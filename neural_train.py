import pandas as pd

from module.separateData import *

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization 
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTETomek
from imblearn.under_sampling import TomekLinks




X = pd.read_csv("data/X_train_reg.csv", index_col=0)
Y = pd.read_csv("data/Y_train.csv" ,index_col = 0)


# nombre de sortie
X,Y,_ = sep(X,Y)
# X,Y,_ -> prédire uniquement les medailles quand il y a des medailles, 3 sorties
# _,_,Y -> prédire si il y a une medaille ou non, 2 sortie
# commenté : 4 sortie



nb_inputs = X.columns.size

# Undersampling
# smote = TomekLinks(sampling_strategy='majority')
# X, Y = smote.fit_resample(X.to_numpy(), Y.to_numpy()) 

print(X)
print(Y)


model = Sequential()


numPerLayer = 9
layerNumber = 10

model.add(BatchNormalization(input_shape = (nb_inputs,)))
model.add(Dropout(0.2))

for i in range(layerNumber):
    model.add(Dense(numPerLayer,  activation='leaky_relu'))
    model.add(Dropout(0.2))

model.add(Dense(3,  activation='softmax'))

model_checkpoint_callback = keras.callbacks.ModelCheckpoint("nn/checkpoint.model.keras")
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), loss="categorical_crossentropy",metrics=['accuracy'])



history = model.fit(X, Y, epochs=5000, batch_size=64, verbose=1,callbacks=[model_checkpoint_callback])
                    #class_weight = {0:1,1:4})
#                    class_weight = {0:0.8468,1:0.8468,2:0.8468,3:0.05})





