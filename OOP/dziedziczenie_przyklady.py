class Animal:

    def __init__(self, name):
        self.name = name
        self.energy = 100

    @property
    def is_alive(self):
        return self.energy > 0

    def move(self, distance):
        self.energy -= 0.1 * distance
        if self.is_alive:
            return distance
        return self.is_alive

    def eat(self, calories):
        self.energy += 0.2 * calories

    def sound(self):
        print("Make NOISE")

a = Animal("Zenek")
print(a.move(50))
print(a.move(5000))

class Dog(Animal):

    def __init__(self, name, species):
        # super().__init__(name) # tak lub tak jak poniżej
        # Animal.__init__(self, name)
        super(Dog, self).__init__(name) # druga opcja użycia "super"
        self.species = species

    def bark(self):
        super().sound()
        print("How How")
        self.energy -= 0.01

a = Animal("Zenek")
azor = Dog("Azor", "Buldog")
print(azor.move(50))
print(azor.bark())
# print(a.bark())
#   File "C:/Users/kurs/PycharmProjects/pythonalx/OOP/dziedziczenie_przyklady.py", line 34, in <module>
#     print(a.bark())
# AttributeError: 'Animal' object has no attribute 'bark'