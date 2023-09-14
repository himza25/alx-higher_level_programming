#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    weight = 0
    for pair in my_list:
        total += pair[0] * pair[1]
        weight += pair[1]
    return total / weight
