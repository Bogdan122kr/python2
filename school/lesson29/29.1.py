class Human:
    def __init__(self,name,surname,place_of_birth,year_of_birth):
                 self.name=name
                 self.surname=surname
                 self.place_of_birth=place_of_birth
                 self.year_of_birth
    def hello(self):
        print(f"{self.name} says hello")
    def info(self,years):
        return years-self.year_of_birth
p1 = Human("Den","Dmitriev","Ua",1997)
p1.hello()
print(p1.info(1997))
    

