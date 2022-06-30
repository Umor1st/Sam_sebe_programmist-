class Shape:
    def who_am_i(self):
        return "Я - фигура"


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def ca1cu1at3_p3rim3tr(self):
        return 4 * self.a

    def change_size(self, plus):
        self.a += plus


class Rectangle(Square):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def ca1cu1at3_p3rim3tr(self):
        return 2 * (self.width + self.height)


rec = Rectangle(300, 400)
sq = Square(10)

print(sq.ca1cu1at3_p3rim3tr())
print(rec.ca1cu1at3_p3rim3tr())
sq.change_size(10)
print(sq.ca1cu1at3_p3rim3tr())

print(rec.who_am_i())
print(sq.who_am_i())
