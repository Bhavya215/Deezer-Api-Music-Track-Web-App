from flask_principal import Permission, RoleNeed
# list various permission types here

# Create a permission with a single Need, in this case a RoleNeed.
admin_permission = Permission(RoleNeed('Admin'))
manager_permission = Permission(RoleNeed('Manager'))
user_permission = Permission(RoleNeed('User'))