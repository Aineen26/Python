# WAP to print rectangle class with different methods to find
# area and perimeter of rectangle and method for checking is square or not

class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth
    def area(self):
        return self.l* self.b
    def perimeter(self):
        return 2*(self.l * self.b)
    def is_square(self):
        return self.l == self.b

    def display_info(self):
        print(f"Rectangle having size: {self.l} x {self.b}")
        print(f"Area of Rectangle: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Is Square: {self.is_square()}")

rect1 = Rectangle(100, 200)
rect2 = Rectangle(200, 300)
rect3 = Rectangle(300, 400)

rect1.display_info()
rect2.display_info()
rect3.display_info()