#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ Check if obj is an instance of, or inherited from, a_class """
    return isinstance(obj, a_class)

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
