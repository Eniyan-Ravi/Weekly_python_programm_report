#Create an Animal hierarchy with different animal types.
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "bark for water")


class Cat(Animal):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def call(self):
        print(self.name, "calls for water")

d = Dog("Danny", "Labrador")
c = Cat("Kitty", "White")

d.eat()
d.bark()

print()

c.eat()
c.call()

print()
