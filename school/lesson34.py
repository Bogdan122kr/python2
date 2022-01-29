class Animal:
    def __init__(self, species):
        self.species = species
    def animal_info(self):
        print(f"имя - {self.species}")
    def make_sound(self):
        print(f"sound")

class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.species = "Dog"
    def make_sound(self):
        print(f"звук-гав! гав!")

class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.species = "Cat"
    def make_sound(self):
        print(f"звук-мяу!")

arr = ["dog", "cat"]

def show_animal_info(name):
  if name not in arr:
    print("такого животного нет!")
  elif name == "dog":
    name = Dog("sound")
    name.animal_info()
    name.make_sound()
  elif name == "cat":
    name = Cat("sound")
    name.animal_info()
    name.make_sound()

show_animal_info("dog")
show_animal_info("cat")
show_animal_info("book")
