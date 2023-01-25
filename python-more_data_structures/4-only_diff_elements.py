#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    new2 = []
    if not set_1:
        return(set_2)
    if not set_2:
        return(set_1)
    for i in set_1:
        for n in set_2:
            if i == n:
                continue
            else:
                new.append(i)
                new.append(n)
    new2 = set_1.intersection(set_2)
    for a in new:
        for b in new2:
            if b == a:
                new.remove(a)
    return(set(new))
