#!/usr/bin/python3
"""
Module Name: square_module

This module defines Square class

Class:
    Square: Defines a square

Atrribute:
    None
Usage:
    new_square = Square(n)

"""


class Square:
    """
    Initializes a new instance


    Args:
        __size (int): The size

        Return:
            None
    """
    def __init__(self, size=0):
        """
        Initializes a new instance

        Args:
            size (int): The size

        Raises:
            TypeError: If size is not an integer
            ValueError: If size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
