class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return 0.5 * self.a * self.h


Triangle = Triangle(1, 2)
print(Triangle.area())
