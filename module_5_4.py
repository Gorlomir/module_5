class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):

        instance = super().__new__(cls)

        cls.houses_history.append(args[0])

        return instance

    def __init__(self, name, number_of_floors):

        self.name = name

        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor < 1:

            print("Такого этажа не существует")

        elif new_floor > self.number_of_floors:

            print("Такого этажа не существует")

        else:

            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):

        return self.number_of_floors

    def __str__(self):

        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):

        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

        return False

    def __lt__(self, other):

        if isinstance(other, House):

            return self.number_of_floors < other.number_of_floors

        elif isinstance(other, int):

            return self.number_of_floors < other

        return NotImplemented

    def __le__(self, other):

        if isinstance(other, House):

            return self.number_of_floors <= other.number_of_floors

        elif isinstance(other, int):

            return self.number_of_floors <= other

        return NotImplemented

    def __gt__(self, other):

        if isinstance(other, House):

            return self.number_of_floors > other.number_of_floors

        elif isinstance(other, int):

            return self.number_of_floors > other

        return NotImplemented

    def __ge__(self, other):

        if isinstance(other, House):

            return self.number_of_floors >= other.number_of_floors

        elif isinstance(other, int):

            return self.number_of_floors >= other

        return NotImplemented

    def __ne__(self, other):

        if isinstance(other, House):

            return self.number_of_floors != other.number_of_floors

        elif isinstance(other, int):

            return self.number_of_floors != other

        return NotImplemented

    def __add__(self, value):

        if isinstance(value, int):
            self.number_of_floors += value

            return self

        return NotImplemented

    def __radd__(self, value):

        if isinstance(value, int):
            self.number_of_floors += value

            return self

        return NotImplemented

    def __iadd__(self, value):

        if isinstance(value, int):
            self.number_of_floors += value

            return self

        return NotImplemented

    def __del__(self):

        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Горский', 10)

h2 = House('Домик в деревне', 20)

h3 = House('ЖК Матрёшки', 20)

print(h1)
print(h2)

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

print(House.houses_history) 

del h2

print(House.houses_history)

print("Домик в деревне снесён, но он останется в истории")
