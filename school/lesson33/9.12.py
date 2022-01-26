from User import *
from Privileges import *
admin = Admin('Саша','Терещенко')
admin.privileges.privileges = [' может добавлять новости',' может удалять новости',' может банить пользователей']
admin.privileges.show_privileges()
