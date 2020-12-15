#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
       lst = reversed(my_list)
       for i in lst:
           print("{:d}".format(i))
