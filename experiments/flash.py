import random
from data.data_to_use import data_albrecht
from experiments.learners import CART

random.seed(1)
all_case = set(range(0, 2880))
initial_pool = random.sample(all_case, 10)


def convert(id):
    a = int(id / 240 + 1)
    b = int(id % 240 / 20 + 1)
    c = int(id % 20 + 1)
    return a, b, c


List_X = []
List_Y = []
for i in range(10):
    List_X.append(convert(initial_pool[i]))
    List_Y.append(CART(data_albrecht(), a=convert(initial_pool[i])[0],
                       b=convert(initial_pool[i])[1], c=convert(initial_pool[i])[2]))

print(List_X)
print(List_Y)