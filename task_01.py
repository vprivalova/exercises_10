class Circle:
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        space = (self.radius**2) * Circle.pi
        return space

    def __str__(self):
        return str(self.radius)

    @staticmethod
    def total_area():
        total = 0
        for elem in Circle.all_circles:
            total += Circle.area(elem)
        return total


c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))
