class Animals:
    def __init__(self,name,age,color,studu,time):
        self.name=name
        self.age=age
        self.color=color
        self.studu=studu
        self.time=time
    def info(self):
        print(f"Name:{self.name},Age:{self.age},Color:{self.color},Studu:{self.studu},Time:{self.time}")

class Dog(Animals):
    def dog(self):
        print(f"Dog:{self.name}DogI")

    def breakfest(self):
        print(f"Он ест в 2 часа дня)

class Cat(Animals):
    def cat(self):
        print(f"Cat:{self.name}CatI")
              
    def seating(self):
        print(f"Он сидит по много часов в день)

class Frog(Animals):
    def frog(self):
        print(f"Frog:{self.name}Frog")

new_s=Dog("Dog",1,"Black","Eating","2 minuts")
new_s.info()
print ("----"*20)
new_s=Cat("Cat",12,"Grey","seating","2 hours")
new_s.info()
print ("----"*20)
new_s=Frog("Frog",24,"Green","KVA-kVa-KvA","5 second")
new_s.info()
print ("----"*20)
