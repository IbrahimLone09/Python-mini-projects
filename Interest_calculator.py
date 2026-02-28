def compound_interest():
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle amount can not be less than or equal to zero:")

    interest_rate = float(input("Enter the interest rate : "))
    if interest_rate <= 0:
        print("Interest rate can not be less than or equal to zero:")


    time = float(input("Enter the time: "))
    if time <= 0:
        print("Time can not be less than or equal to zero:")

    total = principle * pow((1 + interest_rate/100) , time)

    print(f"Balance after {time} is: ${total:.1f}")


def simple_interest():
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle amount can not be less than or equal to zero:")

    interest_rate = float(input("Enter the interest rate : "))
    if interest_rate <= 0:
        print("Interest rate can not be less than or equal to zero:")


    time = float(input("Enter the time: "))
    if time <= 0:
        print("Time can not be less than or equal to zero:")

    total = (principle * interest_rate * time)/100

    print(f"Balance after {time} is: ${total:.1f}")


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







        







