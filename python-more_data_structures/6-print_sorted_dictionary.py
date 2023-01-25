#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    dicc_sorted = {i: a_dictionary[i] for i in keys}
    for key, value in dicc_sorted.items():
        print("{}: {}".format(key, value))
