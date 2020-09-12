#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
from scipy.stats import entropy

def get_entropy(cls):
    total = sum(cls.values())
    p_list = []

    for val in cls.values():
        p_list.append(val / total)

    return entropy(p_list, base=2)


def get_gini(cls):
    total = sum(cls.values())
    val_list = np.array(list(cls.values()))
    p_list = np.true_divide(val_list, total)
    gini = 1 - np.sum(np.power(p_list, 2))

    return gini


gini_parent = 0

if __name__ == '__main__':
    cls = {'YES':4, 'NO':3}
    print("Entropy:", get_entropy(cls))
    gini_parent = get_gini(cls)
    print("Gini:", gini_parent)
