#!/usr/bin/python3

"""
function contains inhert class details
"""

def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited (directly or indirectly)"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
