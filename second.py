num = int(input('Type 1, 2 or 3: '))
if num == 1:
    print('Hello World')
elif num == 2:
    a = 10
    b = 20
    print(a + b)
elif num == 3:
    name = 'Oleksandr'
    surname = 'Lobchenko'
    age = 17
    cost_of_bread = '200 zł'
    s = ''
    s += str(name) + ' ' + str(surname) + ' ' + str(age) + ' ' + str(cost_of_bread)
    print(s)