#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    if my_list is None:
        return
    for i in my_list:
        if i not in new:
            new.append(i)
    return sum(new)
