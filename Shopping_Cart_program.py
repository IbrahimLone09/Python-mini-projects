print("Welcome to the shopping cart!")

print("Please select the items given below!")

print("1 for house hold items:")
print("2 for electronics items")


def house_items():
        print("you chose house hold items!")
        price = float(input("What is the price on one item?: "))
        quantity = int(input("How many would you like?: "))
        total = price * quantity
        print(f"your total is: ${total}")
        print("please visit again!")


def electronics_items():
        print("you chose electronics items!")
        price = float(input("What is the price on one item?: "))
        quantity = int(input("How many would you like?: "))
        total = price * quantity
        print(f"your total is: ${total}")
        print("please visit again!")


while True:
        item = int(input("Which item would you like to buy? "))
        if item == 1:
                house_items()
                break
        elif item == 2:
                electronics_items()
                break 



