import math

class Shape:
    def calculate_area(self):
        pass

    def __int__(self):
        return int(round(self.calculate_area()))

    def __str__(self):
        return "Shape"


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle - Length: {self.length}, Width: {self.width}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle - Radius: {self.radius}"

class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Right Triangle - Base: {self.base}, Height: {self.height}"

class Trapezoid(Shape):
    def __init__(self, upper_base, lower_base, height):
        self.upper_base = upper_base
        self.lower_base = lower_base
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.upper_base + self.lower_base) * self.height

    def __str__(self):
        return f"Trapezoid - Upper Base: {self.upper_base}, Lower Base: {self.lower_base}, Height: {self.height}"


# Example of using the classes:

rectangle = Rectangle(5, 8)
print(f"Area of the rectangle: {int(rectangle)}")
print(str(rectangle))

circle = Circle(3)
print(f"Area of the circle: {int(circle)}")
print(str(circle))

right_triangle = RightTriangle(4, 6)
print(f"Area of the right triangle: {int(right_triangle)}")
print(str(right_triangle))

trapezoid = Trapezoid(5, 7, 10)
print(f"Area of the trapezoid: {int(trapezoid)}")
print(str(trapezoid))
