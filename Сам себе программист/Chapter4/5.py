"""
Програма берет пользовательский ввод и преобразует его в type - float
"""
n = input()
try:
    print(float(n))
except:
    print("Нужно ввести чиcло - а не строку")
