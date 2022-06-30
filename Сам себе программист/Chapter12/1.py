class Apple:
    def __init__(self, color, yammy_score, procent_of_red, weight):
        self.color = color
        self.yammy_score = yammy_score
        self.procent_of_red = procent_of_red
        self.weight = weight
        print("Yammy apple how their actions")


ANTON = Apple("yellow", 100, 0, 500)
print("Це вес яблока:", ANTON.weight)
print("Процент красности:", ANTON.procent_of_red)

