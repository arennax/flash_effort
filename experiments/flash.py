import random
from data.data_to_use import data_albrecht
from experiments.learners import CART
import numpy as np
from sklearn.tree import DecisionTreeRegressor


def convert(index):
    a = int(index / 240 + 1)
    b = int(index % 240 / 20 + 1)
    c = int(index % 20 + 2)
    return a, b, c


def FLASH():
    # random.seed(1)
    all_case = set(range(0, 2880))
    initial_pool = random.sample(all_case, 10)
    life = 10
    List_X = []
    List_Y = []

    while life > 0:
        i = 0
        for i in range(10 + i):
            List_X.append(convert(initial_pool[i]))
            List_Y.append(CART(data_albrecht(), a=convert(initial_pool[i])[0],
                               b=convert(initial_pool[i])[1], c=convert(initial_pool[i])[2]))

        # print(List_X)
        # print(List_Y)

        upper_model = DecisionTreeRegressor()
        upper_model.fit(List_X, List_Y)

        remain_pool = all_case - set(initial_pool)

        test_list = []
        for i in list(remain_pool):
            test_list.append(convert(i))

        # print(test_list)
        p1 = upper_model.predict(test_list)

        # print(p1, np.argmin(p1), p1[np.argmin(p1)], min(p1))
        new_member = np.argmin(p1)   ### there have bugs
        initial_pool += [new_member]
        i += 1
        # remain_pool -= {new_member}

        new_member_mre = CART(data_albrecht(), a=convert(new_member)[0], b=convert(new_member)[1],
                              c=convert(new_member)[2])
        if new_member_mre > np.median(List_Y):
            life -= 1

    print(List_X)
    print(len(List_X))
    print(initial_pool)
    print(len(initial_pool))
    print(np.argmin(initial_pool))
    return np.argmin(initial_pool)



if __name__ == '__main__':
    FLASH()