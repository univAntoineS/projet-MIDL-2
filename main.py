import pandas as pd
from module.addData import *
from sklearn.model_selection import train_test_split 
from module.encode import * 
from module.imputation import *
import datetime
from time import sleep



inp = input("1 : addData\n2 : load data\n> ")

if inp == "1":
    data = pd.read_csv("data/base/athlete_events.csv")

    # add Data

    data = data[data["Season"]!="Winter"]

    data = addAll(data,["NOC"])
    data.to_csv("data/data.csv")

else :
    data = pd.read_csv("data/data.csv",index_col="ID")
# split

train_data, test_data = train_test_split(data, test_size=0.2, random_state = 12) 
toDropInputs = ["Name","Team","Games","Season","City","Year"]
inputs = ["Sex","Age","Height","Weight","NOC","Year","Sport","Event","NbPriorParticipation","PriorGold","PriorSilver","PriorBronze","thisYearParticipation","is_country_hosting","priorGoldPercentForNOC","priorSilverPercentForNOC","priorBronzePercentForNOC"]#,"priorGoldPercentForEvent","priorSilverPercentForEvent","priorBronzePercentForEvent"]

X_train = train_data.drop(toDropInputs,axis = 1).drop("Medal",axis = 1)
Y_train = train_data["Medal"]

X_test = test_data.drop(toDropInputs,axis = 1).drop("Medal",axis = 1)
Y_test = test_data["Medal"]

print(X_train.columns)

# encode


X_train = ordE(X_train,["NOC","Sport","Event"])
X_test = ordE(X_test,["NOC","Sport","Event"])

# impute


X_train_reg = imputation(X_train)
X_test_reg = imputation(X_test)

X_train_mean = X_train.copy()
X_train_mean['Height']=X_train_mean['Height'].fillna(round(X_train_mean["Height"].mean()))
X_train_mean['Weight']=X_train_mean['Weight'].fillna(round(X_train_mean["Weight"].mean()))
X_train_mean['Age']=X_train_mean['Age'].fillna(round(X_train_mean["Age"].mean()))


X_test_mean = X_test.copy()
X_test_mean['Height']=X_test_mean['Height'].fillna(round(X_test_mean["Height"].mean()))
X_test_mean['Weight']=X_test_mean['Weight'].fillna(round(X_test_mean["Weight"].mean()))
X_test_mean['Age']=X_test_mean['Age'].fillna(round(X_test_mean["Age"].mean()))



# 
Y_train = ohe(Y_train,["Medal"])
Y_test = ohe(Y_test,["Medal"])

Y_train = Y_train.loc[:, ["Gold", "Silver", "Bronze","nan"]]
Y_test = Y_test.loc[:, ["Gold", "Silver", "Bronze","nan"]]


X_train_reg.to_csv("data/X_train_reg.csv")
X_test_reg.to_csv("data/X_test_reg.csv")

X_train_mean.to_csv("data/X_train_mean.csv")
X_test_mean.to_csv("data/X_test_mean.csv")

Y_train.to_csv("data/Y_train.csv")
Y_test.to_csv("data/Y_test.csv")
