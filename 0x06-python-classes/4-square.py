#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines the square."""

    def __init__(self, size=0):
        """constructor.

        Args:
            size: len of a square side.
        """
        self.size = size

    @property
    def size(self):
        """Property for the len of a side of the square.

        Raises
            TypeError: if size not int
            ValueError: if size <= 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size ** 2
