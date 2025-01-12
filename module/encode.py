import pandas as pd


#data = pd.read_csv('data/data.csv')

import category_encoders as ce


def ordE(X,columns):
    encoder = ce.OrdinalEncoder(cols=columns)
    
    Y = pd.DataFrame(X)
    Y['val'] = 0
    Y = Y['val']

    return encoder.fit_transform(X,Y,verbose=2,return_df=True)

def loo(X,columns): 
    encoder = ce.LeaveOneOutEncoder(cols=columns)
    
    Y = pd.DataFrame(X)
    Y['val'] = 0
    Y = Y['val']

    print(encoder.fit_transform(X,Y,verbose=2,return_df=True)[["NOC","Sport","Event"]])

    return encoder.fit_transform(X,Y,verbose=2,return_df=True)

def ohe(X,columns):
    encoder = ce.OneHotEncoder(cols=columns)

    Y = pd.DataFrame(X)
    Y['val'] = 0
    Y = Y['val']

    encoded = encoder.fit_transform(X,Y,verbose=2,handle_missing ="ignore",return_df=True)
    
    lst = []

    lst.append(str(X[encoded["Medal_1"] == 1].iloc[0]))
    lst.append(str(X[encoded["Medal_2"] == 1].iloc[0]))
    lst.append(str(X[encoded["Medal_3"] == 1].iloc[0]))
    lst.append(str(X[encoded["Medal_4"] == 1].iloc[0]))
    encoded.columns = lst
    
    return encoded

