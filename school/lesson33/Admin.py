class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("The user's name is " + self.first_name + self.last_name)

    def greet_user(self):
        print("Hello," + self.first_name + self.last_name)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = Privileges()

class Privileges():
    def __init__(self,privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("Admin" + privilege)

admin = Admin('Богдан','Кинах')
admin.privileges.privileges = [' может добавлять новости',' может удалять новости',' может банить пользователей']
admin.privileges.show_privileges()
