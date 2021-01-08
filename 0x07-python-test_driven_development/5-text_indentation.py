#!/usr/bin/python3
"""prints a text with 2 new lines after each of
   these characters: ., ? and :
"""


def text_indentation(text):
    """prints indented text.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = 0
    new_string = ""
    for i in text:
        if flag == 1:
            new_string = ""
            flag = 0
        if i not in "?:.":
            new_string += i
        else:
            new_string += i
            print(new_string.strip())
            print()
            flag = 1
    if flag == 0 and '\n' not in new_string:
        print(new_string.strip(), end="")
    elif flag == 0:
        print(new_string.strip())
