#!/usr/bin/python3
def add_attribute(obj, name, value):
    """Add attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
