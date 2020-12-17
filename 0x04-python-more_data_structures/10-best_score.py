#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > biggest:
                biggest = a_dictionary[key]
                best = key
        return best
