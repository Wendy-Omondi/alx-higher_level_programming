#!/usr/bin/python
def new_in_list(my_list, idx, element):
    mylist = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        mylist[idx] = element
    return mylist
