class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person created")
    def hello(self):
        print(f"{self.name} says hello")
class Student(Human):
    def study(self):
        print(f"{self.name} studing")
class teacher(Human):
    def teach(self):
        print(f"{self.name}-teachs,age:{self.age}")
#s1=Student("zeka",17)
#t1=teacher("Sasha",16)
#s2=Student("Vova",15)
#t2=teacher("Vlad",16)
#s1.hello()
#s2.hello()
#t1.hello()
#t2.hello()
    
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person created")
    def hello(self):
        print(f"{self.name} says hello")
class Student(Human):
    def study(self):
        print(f"{self.name} studing")
    def hello(self):
        print(f"Student created,{self.name} not slys hello")
        S1.hello()
        class teacher(Human):
    def teach(self):
        print(f"{self.name}-teachs,age:{self.age}")
        
        
