# calling class from module
from try_it_yourself_9_7_admin import Privileges

admin = Privileges()
# creating a variable for the imported class
# calling the class directly is enough
admin.show_privileges()
# calling a method in the class to print privileges
# but if we specifically want to call this method we need to define privileges
