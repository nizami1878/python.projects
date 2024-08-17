class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,growth,width):
        self.growth=growth
        self.width=width
    def area(self):
        return self.growth*self.width
shapes=[Circle(9),Rectangle(7,8)]
for shape in shapes:
    print(f"Area: {shape.area()}")