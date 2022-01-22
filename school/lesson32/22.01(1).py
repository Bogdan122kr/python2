#A
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_user(self):
        print(self.first_name,self.last_name)
    def greeting_user(self):
        print(f"Привет, {self.first_name} {self.last_name}")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
        
#c
class Admin(User):
    def __init__(self,first_name,last_name):
        User.__init__(self,first_name,last_name)
        self.privileges=["Allowed to delete users","Allowed to add message","Allowed to ban users"]
    def dreeting_admin(self):
        print(f"Приветствую администрацию, {self.first_name} {self.last_name}!")    
    def show_privileges(self):
        print("Привилегии админа:")
        for i in self.privileges:
            print(i)
class Privileges(Admin):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=["Allowed to delete users","Allowed to add message", "Allowed to ban users"]
    

User = User("Богдан","Кинах")
User.describe_user()
User.greeting_user()

User.increment_login_attempts()
print(User.login_attempts)
User.increment_login_attempts()
print(User.login_attempts)
User.increment_login_attempts()
print(User.login_attempts)
User.reset_login_attempts()
print(User.login_attempts)
Admin=Admin("Богдан","Кинах")
Admin.dreeting_admin()
priv=Privileges("Богдан","Кинах")
priv.show_privileges()
