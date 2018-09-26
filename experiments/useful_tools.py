from sklearn.model_selection import KFold
from sklearn.utils import shuffle
from sklearn import preprocessing
import pandas as pd
import numpy as np


def KFold_df(df, folds=3):
    kf = KFold(n_splits=folds)
    df = shuffle(df)

    for train, test in kf.split(df.index):
        trainData = df.iloc[train]
        testData = df.iloc[test]
        yield trainData, testData


def normalize(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(df)
    df_normalized = pd.DataFrame(np_scaled, columns=df.columns, index=df.index)
    lst_col = df.columns[-1]
    df_normalized[lst_col] = df[lst_col]
    return df_normalized


def mre_calc(y_predict, y_actual):
    mre = []
    for predict, actual in zip(y_predict, y_actual):
        mre.append(abs(predict - actual) / (actual))
    mMRE = np.median(mre)
    if mMRE == 0:
        mMRE = np.mean(mre)
    return mMRE


def sa_calc(Y_predict, Y_actual):
    ar = 0
    for predict, actual in zip(Y_predict, Y_actual):
        ar += abs(predict - actual)
    mar = ar / (len(Y_predict))
    marr = sum(Y_actual) / len(Y_actual)
    sa_error = (1 - mar / marr)
    return sa_error