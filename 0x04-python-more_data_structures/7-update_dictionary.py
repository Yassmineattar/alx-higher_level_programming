#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    tmp = {key: value}
    a_dictionary.update(tmp)
    return (a_dictionary)
