#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = 0
    for x in set(my_list):
        new_list += x
    return (new_list)
