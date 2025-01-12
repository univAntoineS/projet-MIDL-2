import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.under_sampling import RandomUnderSampler
import numpy as np
from sklearn.model_selection import train_test_split 
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("data/data.csv")
data['Medal'].fillna("None", inplace=True)

undersample = RandomUnderSampler(random_state=42)

X = data[["Sex","Age","Height","Weight","NbPriorParticipation","PriorGold","PriorSilver","PriorBronze","thisYearParticipation","is_country_hosting"]]
y = data.Medal

X_over, y_over = undersample.fit_resample(X, y)

# sns.countplot(x=y_over, data=data)
# plt.xticks(rotation=45)
# plt.show()

medal_mapping = {'Gold':1, 'Silver':2, 'Bronze':3, 'None': 4}
y_over=y_over.map(medal_mapping)

X_train, X_test, y_train, y_test = train_test_split(X_over, y_over, random_state=42, shuffle=True, test_size=.2)

X_train_mean = X_train.copy()
X_train_mean['Height']=X_train_mean['Height'].fillna(round(X_train_mean["Height"].mean()))
X_train_mean['Weight']=X_train_mean['Weight'].fillna(round(X_train_mean["Weight"].mean()))
X_train_mean['Age']=X_train_mean['Age'].fillna(round(X_train_mean["Age"].mean()))

X_test_mean = X_test.copy()
X_test_mean['Height']=X_test_mean['Height'].fillna(round(X_test_mean["Height"].mean()))
X_test_mean['Weight']=X_test_mean['Weight'].fillna(round(X_test_mean["Weight"].mean()))
X_test_mean['Age']=X_test_mean['Age'].fillna(round(X_test_mean["Age"].mean()))

st_x = StandardScaler()
X_train = st_x.fit_transform(X_train_mean)
X_test = st_x.transform(X_test_mean)

def logistic_model(C, solver_, multiclass_):
    logistic_regression_model = LogisticRegression(random_state=42, solver=solver_, multi_class=multiclass_, n_jobs=1, C=C)
    return logistic_regression_model

multiclass = ['ovr', 'multinomial']
solver_list = ['liblinear', 'newton-cg', 'lbfgs', 'sag', 'saga']
scores = []
params = []

for i in multiclass:
    for j in solver_list:
        try:
            model = logistic_model(1, j, i)
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            print(predictions)
            params.append(i + ' ' + j)
            accuracy = accuracy_score(y_test, predictions)
            scores.append(accuracy)
        except:
            None

# max=0
# index=0
# for i in range(len(scores)):
#     if scores[i]>max:
#         max=scores[i]
#         index=i
# print(max, index)

# sns.barplot(x=params, y=scores).set_title('Beans Accuracy')
# plt.xticks(rotation=90)
# plt.show()


lm = LogisticRegression(multi_class='ovr', solver='liblinear', class_weight='balanced')
lm.fit(X_train, y_train)

predictions=lm.predict(X_test)
accuracy=accuracy_score(y_test, predictions)
print(accuracy)

class_names = ['Gold', 'Silver', 'Bronze', 'None']
plt.figure(figsize=(12,5))
cm=confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, yticklabels=class_names, xticklabels=class_names, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
#plt.savefig("heatmap.png", dpi=300, bbox_inches='tight')
plt.show()
