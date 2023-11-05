import random

n = int(input("enter the length:"))
list = []
for i in range(n):
    x = (random.randint(1,100))
    if x not in list:
        list.append(x)

for i in range(len(list)):
    print(list[i], end='')
