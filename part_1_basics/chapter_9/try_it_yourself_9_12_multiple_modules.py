from privileges_admin_9_12 import Privileges, Admin

# from the module 'privileges_...' importing two classes

list_privileges = ['add post', 'delete post', 'ban user', 'give privileges']
list_privileges_no_privileges = ["You don't have any privileges"]
# making two lists

admin = Admin('admin', '')
# creating variable called admin adding arguments
admin.message()
# calling message from Admin class
admin.privileges.modify_privileges(list_privileges)
# calling method from Privileges class and list specified above
admin.privileges.show_privileges()
# calling method to print items in the list with for loop
admin.privileges.modify_privileges(list_privileges_no_privileges)
# calling another list but with the same method
print("\n")
admin.message()
admin.privileges.show_privileges()
# printing new list
