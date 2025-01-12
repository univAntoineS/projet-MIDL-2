from sklearn.metrics import accuracy_score
from sklearn.calibration import column_or_1d
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsOneClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression

import pandas as pd

from module.separateData import *

X = pd.read_csv("data/X_train_reg.csv", index_col=0)
Y = pd.read_csv("data/Y_train.csv" ,index_col = 0)



_, _,Y = sep(X,Y)

X = X.to_numpy()

Y = Y.drop("nan",axis=1)
Y = column_or_1d(Y, warn=True)



poly = PolynomialFeatures(degree=3)  # You can change the degree as needed
X = poly.fit_transform(X)


print(X)
print(Y)


model = LogisticRegression(random_state=1, max_iter=1000,verbose=1,class_weight="balanced")
model.fit(X, Y)
print(model.get_params())


print(accuracy_score(Y,model.predict(X))*100)


X = pd.read_csv("data/X_test_reg.csv", index_col=0)
Y = pd.read_csv("data/Y_test.csv" ,index_col = 0)



_, _,Y = sep(X,Y)
X = poly.transform(X.to_numpy())

#X = X.to_numpy()

Y = Y.drop("nan",axis=1)
Y = column_or_1d(Y, warn=False)

print(X)
print(Y)

print(accuracy_score(Y,model.predict(X))*100)


# print(pd.DataFrame(X).to_numpy(),"\n",pd.DataFrame(y).to_numpy())