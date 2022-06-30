class Hexagon:
    def __init__(self, storona):
        self.storona = storona

    def calculate_perimeter(self):
        return self.storona * 6


Hexagon = Hexagon(6)
print(Hexagon.calculate_perimeter())
