from privileges_admin_9_12 import Privileges, Admin

list_privileges = ['add post', 'delete post', 'ban user', 'give privileges']
list_privileges_no_privileges = ["You don't have any privileges"]

admin = Admin('admin', '')
admin.message()
admin.privileges.modify_privileges(list_privileges)
admin.privileges.show_privileges()
admin.privileges.modify_privileges(list_privileges_no_privileges)
print("\n")
admin.message()
admin.privileges.show_privileges()
