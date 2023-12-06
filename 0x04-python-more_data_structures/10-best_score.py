#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    MaxValue = 0
    Maxkey = None
    for k, v in a_dictionary.items():
        if v > MaxValue:
            MaxValue = v
            Maxkey = k
    return Maxkey
