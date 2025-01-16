from classes import *

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h1.go_to(5)
h2.go_to(70)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__