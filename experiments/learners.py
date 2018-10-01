from data.data_to_use import *
from experiments.useful_tools import KFold_df, normalize, mre_calc, sa_calc
import numpy as np
from sklearn.tree import DecisionTreeRegressor


def CART(dataset, a=12, b=1, c=2):

    dataset = normalize(dataset)
    mre_list = []
    sa_list = []
    for train, test in KFold_df(dataset, 3):
        train_input = train.iloc[:, :-1]
        train_actual_effort = train.iloc[:, -1]
        test_input = test.iloc[:, :-1]
        test_actual_effort = test.iloc[:, -1]
        # max_depth: [1:12], min_samples_leaf: [1:12], min_samples_split: [2:21]

        model = DecisionTreeRegressor(max_depth=a, min_samples_leaf=b, min_samples_split=c)
        model.fit(train_input, train_actual_effort)
        test_predict_effort = model.predict(test_input)
        test_predict_Y = test_predict_effort
        test_actual_Y = test_actual_effort.values


        mre_list.append(mre_calc(test_predict_Y, test_actual_Y))   ######### for MRE
        sa_list.append(sa_calc(test_predict_Y, test_actual_Y))   ######### for SA

    mre_mean = np.mean(mre_list)   ######### for MRE
    sa_mean = np.mean(sa_list)   ######### for SA

    return mre_mean   ######### for MRE
    # return sa_mean   ######### for SA


if __name__ == '__main__':
    listA = []
    for i in range(20):
        listA.append(CART(data_albrecht()))
    print(sorted(listA))
