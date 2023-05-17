import math
r = float(input('Type radius of cylinder: '))
h = float(input('Type height of cylinder: '))
S = 2 * math.pi * r**2 + 2 * math.pi * r * h
V = 2 * math.pi * r**2 * h
print('Surface area is ' + str(S))
print('Volume is ' + str(V))