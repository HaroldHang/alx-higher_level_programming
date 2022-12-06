#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = []
    for i in range(0, len(my_list)):
        cp_list.append(my_list[i])
    if idx < 0:
        return cp_list
    elif idx >= len(cp_list):
        return cp_list
    else:
        cp_list[idx] = element
        return cp_list