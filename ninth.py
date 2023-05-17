wyraz = "Co sie dzieja nie wiem"
l_wyraz = wyraz.split(' ')
print(f"Ilość wyrazów: {len(l_wyraz)}")
print(f"Ilość liter: {len(wyraz)}")


box = {}

for x in wyraz:
    if x not in box:
        box.update({x: wyraz.count(x)})


print(box)