#!/usr/bin/python3
def no_c(my_string):
    toreturn = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            toreturn += my_string[i]
        return toreturn
