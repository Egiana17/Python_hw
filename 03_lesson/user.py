From user import User
def get_full_name():
    return (f"name: {first_name} + {last_name}")
my_user = User("Egiana", "Abysheva")
print(my_user.first_name)
print(my_user.last_name)
print(get_full_name())
