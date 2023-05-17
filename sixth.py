import random
s = ''
for x in range(1, 100):
    s += str(random.randint(0, 100)) + ', '
print(s)