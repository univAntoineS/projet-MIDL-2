import pandas as pd



def sep(X,Y):
    medal = pd.DataFrame(index= Y.index)
    medal["Medal"] = (Y["nan"] == 0).astype(int)
    medal["nan"] = Y["nan"]

    X = X[Y["nan"] == 0]
    Y = Y[Y["nan"] == 0].drop("nan",axis=1)
    
    return X,Y,medal


# X = pd.read_csv("data/X_test_reg.csv",index_col=0)
# Y = pd.read_csv("data/Y_test.csv",index_col=0)

# X,Y,medal = sep(X,Y)

# print(X)
# print(Y)
# print(medal)