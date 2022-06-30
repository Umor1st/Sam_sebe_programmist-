import re

stri = "Приведение прошуршало и и исчезло в углу."
p = re.findall(".ло", stri)
print(p)
