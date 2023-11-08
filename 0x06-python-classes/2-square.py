#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """ the square class"""
    def __init__(self, size=0):
        """instantiation"""
        self.__size=size

    @property
    def size(self):
        """getter"""
        return self.__size
    @size.setter
    def size(self, value):
        """setter"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be and int")
        elif value < 0:
            raise ValueError("size must be >= 0")
