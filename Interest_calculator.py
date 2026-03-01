def compound_interest():
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("principal amount can not be less than or equal to zero:")

    interest_rate = float(input("Enter the interest rate : "))
    if interest_rate <= 0:
        print("Interest rate can not be less than or equal to zero:")


    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can not be less than or equal to zero:")

    total = principal * pow((1 + interest_rate/100) , time)

    print(f"compound interest after {time:.0f} years will be: ${(total - principal):.1f}")
    print(f"Balance after {time:.0f} years will be: ${total:.1f}")


def simple_interest():
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("principal amount can not be less than or equal to zero:")

    interest_rate = float(input("Enter the interest rate : "))
    if interest_rate <= 0:
        print("Interest rate can not be less than or equal to zero:")


    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can not be less than or equal to zero:")

    total = (principal * interest_rate * time)/100

    print(f"Simple interest after {time:.0f} years will be: ${total:.1f}")
    print(f"Balance after {time:.0f} years will be: ${total + principal}")


print("Welcome to the interest calculator")
while True:
    choice = input(
    "Please choose the type of interest( simple/compound ) you want to calculate( Q to quit)! ").lower()
    if choice == "q":
        print("Well if you change your mind try again good luck!")
        break

    elif choice == "simple":
        simple_interest()
        break
    
    elif choice == "compound":
        compound_interest()
        break
    else:
        print("Please select the correct option!")







        







