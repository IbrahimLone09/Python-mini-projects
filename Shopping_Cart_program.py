print("Welcome to the shopping cart!")

print("Please select the items given below!")

print("Type '1' for household items:")
print("Type '2' for electronics items")


def house_items():
        print("you chose household items,the item list is given below!")

        print("Type 'A' for furniture(sofa,bed,table)!")
        print("Type 'B' for kitchenware(pots,pans,cutlery)!")
        print("Type 'C' for cleaning supplies(broom,mop,vaccum)!")

        item = input("Type your choices! ")
        if item == "A":
                quantity = float(input("The price for one furniture item is $100,how many would you like? "))
                total = quantity * 100
                print(f"your total is: ${total}")
                print("please visit again!")

        elif item == "B":
                quantity = float(input("The price for one kitchenware item is $50,how many would you like? "))
                total = quantity * 50
                print(f"your total is: ${total}")
                print("please visit again!")

        elif item == "C":
                quantity = float(input("The price for one cleaning supplies item is $40,how many would you like? "))
                total = quantity * 40
                print(f"your total is: ${total}")
                print("please visit again!")

        else:
                print("please next time choose the correct option!")


def electronics_items():
        print("you chose electronics items,the item list is given below!")

        print("Type 'A' for smartphones!")
        print("Type 'B' for refrigerators!")
        print("Type 'C' for audio equipments!")

        item = input("Type your choices! ")
        if item == "A":
                quantity = float(input("The price for one smartphone  item is $800,how many would you like? "))
                total = quantity * 800
                print(f"your total is: ${total}")
                print("please visit again!")

        elif item == "B":
                quantity = float(input("The price for one refrigerstor item is $500,how many would you like? "))
                total = quantity * 500
                print(f"your total is: ${total}")
                print("please visit again!")

        elif item == "C":
                quantity = float(input("The price for one audio equipment item is $300,how many would you like? "))
                total = quantity * 300
                print(f"your total is: ${total}")
                print("please visit again!")

        else:
                print("please next time select the correct option!")



while True:
        item = int(input("Which item would you like to buy? "))
        if item == 1:
                house_items()
                break
        elif item == 2:
                electronics_items()
                break 



