print("Welcome to Password strength checker!")

password = input("Enter your password! ")

special_characters = "!@#$%^&*"

digit_count = 0
upper_count = 0
lower_count = 0
special_count = 0


for char in password:
    if char.isdigit():
        digit_count += 1

    elif char.isupper():
        upper_count += 1

    elif char.islower():
        lower_count += 1

    elif char in special_characters:
        special_count += 1


if len(password) < 6:
    print(f"The passwrod {password} you entered is weak type!")

elif 6 <= len(password) < 10:
     
    type_count = 0
    if digit_count > 0:
        type_count += 1

    if upper_count > 0:
        type_count += 1

    if lower_count > 0:
        type_count += 1

    if special_count > 0:
        type_count += 1

    if type_count <= 2:
        print(f"The password {password} you entered is weak type!")

    else:
       print(f"The password {password} you entered is medium type!")

    
elif len (password) >= 10:

    type_count = 0
    if digit_count > 0:
        type_count += 1

    if upper_count > 0:
        type_count += 1

    if lower_count > 0:
        type_count += 1

    if special_count > 0:
        type_count += 1


    if type_count == 4:
        print(f"The password {password} you entered is strong type!")

    elif type_count >= 2:
        print(f"The password {password} you entered is medium type!")

    else:
        print(f"The password {password} you entered is weak type!")
