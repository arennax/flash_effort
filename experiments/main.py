from data.data_to_use import *
from experiments.learners import CART
from experiments.flash import FLASH
import numpy as np

data = data_kitchenham()


if __name__ == '__main__':
    list_CART = []
    list_FLASH_CART = []
    for i in range(20):
        list_CART.append(CART(data))
        list_FLASH_CART.append(CART(data,a=FLASH(data)[0],b=FLASH(data)[1],c=FLASH(data)[2]))

    print(sorted(list_CART))
    print(sorted(list_FLASH_CART))

    print("median for CART0:", np.median(list_CART))
    print("median for FLASH_CART:", np.median(list_FLASH_CART))