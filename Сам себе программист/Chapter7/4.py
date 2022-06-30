from random import *
sp = [1, 2, 3, 4, 5, 6, 7, 87, 9, 777, 879, 666, 132134]
print("Угадай число из списка")
print(*sp)
i = choice(sp)
while True:
    print("///Введите x чтобы выйти///")
    n = int(input("Введите число ->>"))
    if n == i:
        print("К0лдун ебучий!!!")
        break
    else:
        print("А-а неправильно")
    print(*sp)
