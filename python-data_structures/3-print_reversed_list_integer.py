#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) + 1):
        if my_list:
            if my_list[-i] == 1:
                pass
            elif my_list[i] == None:
                return(None)
            else:
                print("{:d}".format(my_list[-i]))
        else:
            return(None)
    print("{:d}".format(1))
