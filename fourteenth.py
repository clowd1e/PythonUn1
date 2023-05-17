# txt = "I love apples, apple, are my favorite fruit"

# x = txt.count(" apple ")

# if x == 0 :
#     y = txt.count(" apple,")
#     print(y)
# else:
#     print(x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)


def func1(n):
  return lambda a : a // n
myfunc = func1(4)
print(myfunc(2))