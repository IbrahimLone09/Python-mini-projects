print("Choose the options given below!")

print("Enter 1 to convert (kg -> g)!")
print("enter 2 to convert (g -> kg)!")
print("Enter 3 to convert (kg -> lb)!")
print("Enter 4 to convert (lb -> kg)!") 
print("Enter 5 to convert (kg -> oz)!")
print("Enter 6 to convert (oz -> kg)!")


def kg_to_g():
    kilograms = int(input("Enter the kilograms you want to convert! "))
    print("The value in grams will be", kilograms*1000 ,"g")


def g_to_kg():
    grams = int(input("Enter the grams you want to convert! "))
    print("The value in kilograms will be", grams/1000, "kg")


def kg_to_lb():
    kg = int(input("Enter the kilograms you want to convert to pounds! "))
    print("The value in pounds(lb) will be",kg*2.205, "lb")


def  lb_to_kg():
    lb = int(input("Enter the pounds(lb) you want to convert! "))
    print("The value in kilograms will be",lb/2.205, "kg")


def kg_to_oz():
    kgs = int(input("Enter the kilograms(kg) you want to convert to ounces! "))
    print("The value in ounces will be",kgs*35.274, "oz")


def oz_to_kg():
    oz = int(input("Enter the ounces(oz) you want to convert to kilograms! "))
    print("The value in kilograms will be",oz/35.274, "kg")





while True:
    choice = input("Enter your choice! ")
    if choice == "1":
        kg_to_g()
        break

    elif choice == "2":
        g_to_kg()
        break

    elif choice == "3":
        kg_to_lb()
        break

    elif choice == "4":
        lb_to_kg()
        break

    elif choice == "5":
        kg_to_oz()
        break

    elif choice == "6":
        oz_to_kg()
        break

    else:
        print("Please select the correct option!")
        

    




















