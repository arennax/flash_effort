from data.data_to_use import *
from experiments.learners import CART
from experiments.flash import FLASH
import numpy as np
import time

data = data_albrecht()
repeats = 20


if __name__ == '__main__':
    list_CART = []
    list_FLASH_CART = []

    time1 = time.time()
    for i in range(repeats):
        list_CART.append(CART(data))
    run_time1 = str(time.time() - time1)

    time2 = time.time()
    for i in range(repeats):
        tmp = FLASH(data)
        list_FLASH_CART.append(CART(data,a=tmp[0],b=tmp[1],c=tmp[2]))
    run_time2 = str(time.time() - time2)

    print(sorted(list_CART))
    print(sorted(list_FLASH_CART))

    print("median for CART0:", np.median(list_CART))
    print("median for FLASH_CART:", np.median(list_FLASH_CART))

    print("mean for CART0:", np.mean(list_CART))
    print("mean for FLASH_CART:", np.mean(list_FLASH_CART))

    print("runtime for CART0:", run_time1)
    print("runtime for FLASH_CART:", run_time2)

    with open("./output/test_sk.txt", "w") as output:
        for i in sorted(list_FLASH_CART):
            output.write(str(i)+" ")
