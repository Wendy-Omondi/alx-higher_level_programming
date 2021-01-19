#!/usr/bin/python3
"A module that defines a inherited class named MyList"


class MyList(list):
    """
    A class named My List
    """
    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
