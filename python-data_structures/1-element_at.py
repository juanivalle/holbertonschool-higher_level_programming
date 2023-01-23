#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        print("Element at index {:d} is {}".format(idx, None))
    elif idx > len(my_list):
        print("Element at index {:d} is {}".format(idx, None))
    else:
        return(my_list[idx])
