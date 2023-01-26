def best_score(a_dictionary):
    if a_dictionary == None:
        return(None)
    else:
        key_max = max(a_dictionary, key = a_dictionary.get)
    return(key_max)
