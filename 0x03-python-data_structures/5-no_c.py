#!/usr/bin/python3

def no_c(my_string):
    string_edit = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            string_edit += i
    return string_edit
