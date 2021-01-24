class Shape:
    name = ""
    length = 0
    height = 0
    area = 0

    def __init__(self, name, length, height):
        self.name = name
        self.length = length
        self.height = height
        print('create shape -- ', self.name, self.length, self.height)

    def __del__(self):
        print('destroy shape -- ', self.name)


class Square(Shape):
    def area(self):
        print('area of', self.name, ' is ', self.length * self.length)

class Rectangle(Shape):
    def area(self):
        print('area of', self.name, ' is ', self.length * self.height)


shape = Square('square', 10, 10)
shape.area()

shape = Rectangle('rectangle', 10, 20)
shape.area()


