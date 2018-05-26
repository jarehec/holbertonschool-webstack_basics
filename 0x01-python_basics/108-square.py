#!/usr/bin/python3
"""
module containing Square class
"""


class Square:
    """
    defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializing attributes
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position attribute
        """
        if type(value) is tuple and len(value) == 2 and \
           type(value[0]) is int and type(value[1]) is int and \
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """
        return the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        string representation of square
        """
        print('\n' * self.__position[1], end='')
        print('\n'.join([' ' * self.__position[0] +
                         '#' * self.size for i in range(self.size)]))
