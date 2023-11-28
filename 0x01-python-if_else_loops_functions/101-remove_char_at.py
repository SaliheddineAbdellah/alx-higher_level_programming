#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for x in str:
        i++
    if i >= n:
        str[n] = ""
    return str
