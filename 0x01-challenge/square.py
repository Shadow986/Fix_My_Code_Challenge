#!/usr/bin/python3
"""
Web server 
"""
class Square():
    
    side = 0

    def __init__(self, side):
        self.side = side

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def perimeter_of_my_square(self):
        return self.side * 4

    def __str__(self):
        return "Square with side length {}".format(self.side)

if __name__ == "__main__":

    s = Square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
