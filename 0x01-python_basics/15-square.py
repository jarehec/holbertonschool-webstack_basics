#!/usr/bin/python3
"""
module containing Square class
"""


class Square:
    """
    defines a square
    """
    def __init__(self, size=0):
        """
        initializing attributes
        """
        self.size = size

    @property
    def size(self):
        """
        getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size attribute
        """
        if value.__class__ is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        return the area of the square
        """
        return self.size ** 2

    def my_print(self):
        """
        string representation of square
        """
        print('\n'.join(['#' * self.size for i in range(self.size)]))
