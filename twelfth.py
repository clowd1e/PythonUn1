a = int(input('Type number: '))

array = []

if a >= 0:
    if a == 0:
        print(0000)
    else:
        while a > 1:
            array.append(int(a % 2))
            a = a / 2

print(array)

s = ''

for i in range(1, len(array) + 1):
    s += str(array[-i])

print(s)