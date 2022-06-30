class Rider:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, color, weight, owner):
        self.color = color
        self.weight = weight
        self.owner = owner


Kira = Rider("Кира Ишигами")
Loshadka = Horse('red', 500, Kira)
print(Loshadka.owner.name)