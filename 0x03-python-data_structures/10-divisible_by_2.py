#!/usr/bin/python
def divisible_by_2(my_list=[]):
    new_list = [False] * len(my_list)
    if my_list:
        for idx, num in enumerate(my_list):
            if num % 2 == 0:
                new_list[idx] = True
        return new_list
    else:
        return (None)