import random
from data.data_to_use import *
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
    life = 5

    while life > 0:
        List_X = []
        List_Y = []
        for i in range(len(modeling_pool)):
            List_X.append(convert(modeling_pool[i]))
            temp = convert(modeling_pool[i])
            List_Y.append(CART(data_albrecht(), a=temp[0], b=temp[1], c=temp[2]))

        # print(List_X)
        # print(List_Y)

        ### Upper level optimizier (cart)
        upper_model = DecisionTreeRegressor()
        upper_model.fit(List_X, List_Y)

        remain_pool = all_case - set(modeling_pool)

        test_list = []
        for i in list(remain_pool):
            test_list.append(convert(i))

        # print(test_list)
        p1 = upper_model.predict(test_list)

        # acquisition function
        # new_member = list(remain_pool)[np.argmin(p1).item()]  ######### for MRE
        new_member = list(remain_pool)[np.argmax(p1).item()]  ######### for SA
        modeling_pool += [new_member]
        new_config = convert(new_member)
        new_member_fitness = CART(dataset, a=new_config[0], b=new_config[1], c=new_config[2])

        # if new_member_fitness > np.median(List_Y):   ######### for MRE
        if new_member_fitness < np.median(List_Y):   ######### for SA
            life -= 1

    final_X = []
    final_Y = []
    for i in range(len(modeling_pool)):
        final_X.append(convert(modeling_pool[i]))
        final_config = convert(modeling_pool[i])
        final_Y.append(CART(data_albrecht(), a=final_config[0], b=final_config[1], c=final_config[2]))

    # best_index = np.argmin(final_Y)   ######### for MRE
    best_index = np.argmax(final_Y)   ######### for SA
    best_config_id = modeling_pool[best_index]
    best_config = convert(best_config_id)

    return best_config


if __name__ == '__main__':
    print(FLASH(data_finnish()))
