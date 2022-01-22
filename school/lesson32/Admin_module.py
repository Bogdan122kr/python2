from user  import *
from Admin  import *
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
