#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0
    under = 0
    weight = 0
    for t in my_list:
        under += t[1]
        weight += t[0] * t[1]
    return weight / under
