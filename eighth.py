import random

array = []

for i in range(random.randint(1, 20)):
    array.append(random.randint(-100, 0))

print(array)
print(max(array))