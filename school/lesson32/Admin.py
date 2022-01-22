from user import *
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
