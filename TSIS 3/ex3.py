class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shape = Shape()
print("Area of shape:", shape.area())

square = Square(5)
print("Area of square:", square.area())

rectangle = Rectangle(4, 6)
print("Area of rectangle:", rectangle.area())

