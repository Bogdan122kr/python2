from user  import *
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
