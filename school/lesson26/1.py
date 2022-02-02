class Human:
    def __init__(self,name,surname,age,birth):
        self.name=name
        self.surname=surname
        self.age=age
        self.birth=birth

    def info(self):
        print(f"NAME:{self.name},surname:{self.surname},age:{self.age},birth:{self.birth} ")

class Student(Human):
    def study(self):
        print(f"Student:{self.name} studding")

class Techer(Human):
    def teach(self):
        print(f"Student:{self.name} teaching")

new_s=Student("Bogdan","Kinakh","KR",2003)
new_s.info()

