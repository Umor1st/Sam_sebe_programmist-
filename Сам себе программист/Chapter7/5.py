l1 = [8, 19, 148, 4]
l2 = [9, 1, 33, 83]
last = []
for i in l1:
    for j in l2:
        last.append(i*j)
print(*last)