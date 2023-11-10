#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = dict(a_dictionary)
    for i in a.keys():
        a[i] *= 2
    return (a)
