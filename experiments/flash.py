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


def FLASH(dataset):
    # random.seed(1)
    all_case = set(range(0, 2880))
    modeling_pool = random.sample(all_case, 10)
    life = 3

    while life > 0:
        List_X = []
        List_Y = []
        for i in range(len(modeling_pool)):
            List_X.append(convert(modeling_pool[i]))
            List_Y.append(CART(data_albrecht(), a=convert(modeling_pool[i])[0],
                               b=convert(modeling_pool[i])[1], c=convert(modeling_pool[i])[2]))

        # print(List_X)
        # print(List_Y)

        upper_model = DecisionTreeRegressor()
        upper_model.fit(List_X, List_Y)

        remain_pool = all_case - set(modeling_pool)

        test_list = []
        for i in list(remain_pool):
            test_list.append(convert(i))

        # print(test_list)
        p1 = upper_model.predict(test_list)

        # print(p1, np.argmin(p1), p1[np.argmin(p1)], min(p1))
        new_member = list(remain_pool)[np.argmin(p1)]   ### there have bugs
        modeling_pool += [new_member]
        # remain_pool -= {new_member}

        new_member_mre = CART(dataset, a=convert(new_member)[0], b=convert(new_member)[1],
                              c=convert(new_member)[2])
        if new_member_mre > np.median(List_Y):
            life -= 1

    final_X = []
    final_Y = []
    for i in range(len(modeling_pool)):
        final_X.append(convert(modeling_pool[i]))
        final_Y.append(CART(data_albrecht(), a=convert(modeling_pool[i])[0],
                           b=convert(modeling_pool[i])[1], c=convert(modeling_pool[i])[2]))

    best_index = np.argmin(final_Y)
    best_config_id = modeling_pool[best_index]
    best_config = convert(best_config_id)

    return best_config


if __name__ == '__main__':
    print(FLASH(data_albrecht()))
