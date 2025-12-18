user_name = input("Enter name: ")

if len(user_name) >= 3:
    print("Hello <<UserName>>, How are you?".replace("<<UserName>>", user_name))
else:
    print("Name must have at least 3 characters")
