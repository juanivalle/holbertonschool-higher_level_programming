#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return(None)
    elif not a_dictionary:
        return(None)
    else:
        key_max = max(a_dictionary, key=a_dictionary.get)
    return(key_max)
