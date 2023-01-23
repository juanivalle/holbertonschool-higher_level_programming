#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(0, len(my_list)):
        if idx < 0 or idx > len(my_list):
            return(none)
        else:
            print("Element at index {:d} is {}".format(idx, my_list[idx]))
