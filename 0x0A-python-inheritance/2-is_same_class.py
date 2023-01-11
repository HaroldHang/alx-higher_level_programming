#!/usr/bin/python3
"""Check the class nature of an object
"""

def is_same_class(obj, a_class):
    """Returs if True if is intance of
    a_class otherwise false
    """
    return (type(obj) == a_class)
