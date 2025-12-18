user_name = input("Enter name: ")

if len(user_name) >= 3:
    print(f"Hello {user_name}, How are you?")
else:
    print("Name must have at least 3 characters")
