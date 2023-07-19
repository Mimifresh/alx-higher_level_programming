#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        denomination = 0
        for tup in my_list:
            number += (tup[0] * tup[1])
            denomination += (tup[1])
        return (num/denom)
    return 0
