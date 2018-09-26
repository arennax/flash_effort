from data.data_to_use import data_albrecht
from experiments.useful_tools import KFold_df, normalize, mre_calc
import numpy as np
from sklearn.tree import DecisionTreeRegressor


def CART(dataset):

    dataset = normalize(dataset)
    mre_list = []
    mre_mean = 0
    for train, test in KFold_df(dataset, 3):
        train_input = train.iloc[:, :-1]
        train_actual_effort = train.iloc[:, -1]
        test_input = test.iloc[:, :-1]
        test_actual_effort = test.iloc[:, -1]
        # max_depth: [1:12], min_samples_leaf: [1:12], min_samples_split: [1:20]
        model = DecisionTreeRegressor(max_depth=12, min_samples_leaf=1, min_samples_split=2)
        model.fit(train_input, train_actual_effort)
        test_predict_effort = model.predict(test_input)
        test_predict_Y = test_predict_effort
        test_actual_Y = test_actual_effort.values

        # print(mre_calc(test_predict_Y, test_actual_Y))
        mre_list.append(mre_calc(test_predict_Y, test_actual_Y))
        mre_mean = np.mean(mre_list)

    return mre_mean


if __name__ == '__main__':
    listA = []
    for i in range(20):
        listA.append(CART(data_albrecht()))
    print(sorted(listA))
