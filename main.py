class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def show(self):
        pass

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.shape_type}\n")
            for key, value in self.__dict__.items():
                file.write(f"{key}: {value}\n")

    def load(self, filename):
        with open(filename, 'r') as file:
            shape_type = file.readline().strip()
            data = {}
            for line in file:
                key, value = map(str.strip, line.split(':'))
                data[key] = int(value) if value.isdigit() else value
            data['shape_type'] = shape_type
            return data

class Square(Shape):
    def __init__(self, left_top_x, left_top_y, side_length, shape_type='Square'):
        super().__init__(shape_type)
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.side_length = side_length

    def show(self):
        print(f"Type: {self.shape_type}, Left Top: ({self.left_top_x}, {self.left_top_y}), Side Length: {self.side_length}")

class Rectangle(Shape):
    def __init__(self, left_top_x, left_top_y, width, height):
        super().__init__('Rectangle')
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.width = width
        self.height = height

    def show(self):
        print(f"Type: {self.shape_type}, Left Top: ({self.left_top_x}, {self.left_top_y}), Width: {self.width}, Height: {self.height}")

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__('Circle')
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        print(f"Type: {self.shape_type}, Center: ({self.center_x}, {self.center_y}), Radius: {self.radius}")

class Ellipse(Shape):
    def __init__(self, left_top_x, left_top_y, width, height):
        super().__init__('Ellipse')
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.width = width
        self.height = height

    def show(self):
        print(f"Type: {self.shape_type}, Left Top: ({self.left_top_x}, {self.left_top_y}), Width: {self.width}, Height: {self.height}")

print("Square")
square = Square(
    int(input("Enter left top x for square: ")),
    int(input("Enter left top y for square: ")),
    int(input("Enter side length for square: "))
)

print("Rectangle")
rectangle = Rectangle(
    int(input("Enter left top x for rectangle: ")),
    int(input("Enter left top y for rectangle: ")),
    int(input("Enter width for rectangle: ")),
    int(input("Enter height for rectangle: "))
)

print("Circle")
circle = Circle(
    int(input("Enter center x for circle: ")),
    int(input("Enter center y for circle: ")),
    int(input("Enter radius for circle: "))
)

print("Ellipse")
ellipse = Ellipse(
    int(input("Enter left top x for ellipse: ")),
    int(input("Enter left top y for ellipse: ")),
    int(input("Enter width for ellipse: ")),
    int(input("Enter height for ellipse: "))
)

square.save('square.txt')
rectangle.save('rectangle.txt')
circle.save('circle.txt')
ellipse.save('ellipse.txt')

loaded_square_data = Shape('Unknown').load('square.txt')
loaded_rectangle_data = Shape('Unknown').load('rectangle.txt')
loaded_circle_data = Shape('Unknown').load('circle.txt')
loaded_ellipse_data = Shape('Unknown').load('ellipse.txt')

loaded_square = Square(**loaded_square_data)
loaded_rectangle = Rectangle(**loaded_rectangle_data)
loaded_circle = Circle(**loaded_circle_data)
loaded_ellipse = Ellipse(**loaded_ellipse_data)

loaded_square.show()
loaded_rectangle.show()
loaded_circle.show()
loaded_ellipse.show()

