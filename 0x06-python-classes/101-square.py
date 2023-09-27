#!/usr/bin/python3
"""A module containing a class definition for a square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square object with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                any(n < 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square using the '#' character."""
        if self.size == 0:
            print()
            return
        print('\n' * self.position[1], end='')
        for _ in range(self.size):
            print(' ' * self.position[0] + '#' * self.size)

    def __str__(self):
        """Make the class printable."""
        if self.size == 0:
            return ""
        result = []
        result.append('\n' * self.position[1])
        for _ in range(self.size):
            result.append(' ' * self.position[0] + '#' * self.size)
        return '\n'.join(result)


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)
    print("--")
    my_square = Square(5, (4, 1))
    print(my_square)
