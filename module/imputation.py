import pandas as pd


from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression

def imputation(data):
    index = data.index
    imputer = IterativeImputer(estimator=LinearRegression(), verbose=1)

    imData = imputer.fit_transform(data)

    data = pd.DataFrame(imData,columns=data.columns)
    data.set_index(index, inplace=True)
    return data




if __name__ == "__main__":
    data = pd.read_csv("data/base/athlete_event.csv")

    percent_missing = data.isnull().sum() * 100 / len(data)
    missing_value_df = pd.DataFrame({'column_name': data.columns,
                                    'percent_missing': percent_missing})

    print(missing_value_df)


    print(data)
    data.to_csv("data/imputed.csv")