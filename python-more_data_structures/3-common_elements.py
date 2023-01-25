#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    for i in set_1:
        for n in set_2:
            if i == n:
                new.append(i)
    return(set(new))
