class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area not defined")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Circle area: {3.14 *self.radius* self.radius}")
class Rectangle(Shape):
    def __init__(self,lenght,width):
        self.length = lenght
        self.width =width
    def area(self):
        print(f"Rectangle area:{self.length * self.width}")
s = Shape()
c = Circle(5)
r = Rectangle(4,5)
s.area()
c.area()
r.area()