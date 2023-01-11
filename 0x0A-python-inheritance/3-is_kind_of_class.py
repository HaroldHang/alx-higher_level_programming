#!/usr/bin/python3
"""Check the object is a instance of class or a
derived class
"""

def is_kind_of_class(obj, a_class):
    """Returs if True if is intance of
    a_class otherwise false
    """
    return isinstance(obj, a_class)
