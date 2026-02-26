#!/usr/bin/env python3
"""
A simple Python script that prints "Hello, World!" to the console.
"""

import numpy

def hello():
    """
    Returns a greeting message.
    """
    return "Hello, World!" + " " + str(numpy.array([1, 2, 3]))


if __name__ == "__main__":
    print(hello())
