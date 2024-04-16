#!/usr/bin/python3
"""
contain mylist class
"""

class MyList(list):
    """subclass"""
    def __init__(self):
        """initialize"""
        super().__init__()
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
