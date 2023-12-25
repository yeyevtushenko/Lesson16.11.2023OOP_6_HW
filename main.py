import math

class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


class Trapezoid(Shape):
    def __init__(self, upper_base, lower_base, height):
        self.upper_base = upper_base
        self.lower_base = lower_base
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.upper_base + self.lower_base) * self.height




rectangle = Rectangle(5, 8)
print(f"Area of the rectangle: {rectangle.calculate_area()}")

circle = Circle(3)
print(f"Area of the circle: {circle.calculate_area()}")

right_triangle = RightTriangle(4, 6)
print(f"Area of the right triangle: {right_triangle.calculate_area()}")

trapezoid = Trapezoid(5, 7, 10)
print(f"Area of the trapezoid: {trapezoid.calculate_area()}")