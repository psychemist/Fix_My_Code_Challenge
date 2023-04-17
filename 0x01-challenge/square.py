#!/usr/bin/python3
"""square module contains a class that
creates a square and calculates its properties
"""


class Square():
    """
    Creates a Square class object with two public class attributes,
    two public class methods and two private class methods
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes square class instance and populates its dictionary """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ Returns area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Returns perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns a string representation of square instance """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter_of_my_square())
