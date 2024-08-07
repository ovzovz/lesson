import random

first = random.choice(range(3, 21))
#for first in range(3,21):
second = ""
for i in list(range(1, first // 2 + 1)):
    for j in range(i + 1, first):
        if first % (i + j) == 0:
            second += str(i)
            second += str(j)
print(first, " - ", second)
