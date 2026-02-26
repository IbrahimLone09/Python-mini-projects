print("Welcome to the shopping cart!")

print("Please select the items given below!")

print("Type '1' for household items:")
print("Type '2' for electronics items:")
print("Type '3' for mechanical items:")
print("Type '4' for clothing items:")


def house_items():
        print("you chose household items,the item list is given below!")

        print("Type 'A' for furniture(sofa,bed,table)!")
        print("Type 'B' for kitchenware(pots,pans,cutlery)!")
        print("Type 'C' for cleaning supplies(broom,mop,vaccum)!")

        item = input("Type your choices! ").upper()
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

        item = input("Type your choices! ").upper()
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


def mechanical_items():
        print("you chose mechanical items,the item list is given below!")

        print("Type 'A' for fasteners(screws,bolts,nuts)!")
        print("Type 'B' for power transmission(gears,bolts,bearings)")
        print("Type 'C' for hydraulic components!")

        item = input("Type your choices! ").upper()
        if item == "A":
                quantity = float(input("The price for one fastener  item is $400,how many would you like? "))
                total = quantity * 400
                print(f"your total is: ${total}")
                print("please visit again!")

        elif item == "B":
                quantity = float(input("The price for one power transmission item is $900,how many would you like? "))
                total = quantity * 900
                print(f"your total is: ${total}")
                print("please visit again!")

        elif item == "C":
                quantity = float(input("The price for one hydraulic item is 1200,how many would you like? "))
                total = quantity * 1200
                print(f"your total is: ${total}")
                print("please visit again!")

        else:
                print("please next time choose the correct option!")


def clothing_item():
        print("you chose clothing items,the item list is given below!")

        print("Type 'A' for tops(shirts etc)!")
        print("Type 'B' for bottoms(jeans,trousers,skirts)!")
        print("Type 'C' for outerwear(coats,jackets)!")

        item = input("Type your choices! ").upper()
        if item == "A":
                quantity = float(input("The price for one top  item is $150,how many would you like? "))
                total = quantity * 150
                print(f"your total is: ${total}")
                print("please visit again!")

        elif item == "B":
                quantity = float(input("The price for one bottom item is $175,how many would you like? "))
                total = quantity * 175
                print(f"your total is: ${total}")
                print("please visit again!")

        elif item == "C":
                quantity = float(input("The price for one outwear item is $195,how many would you like? "))
                total = quantity * 195
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

        elif item == 3:
                mechanical_items()
                break 
        
        elif item == 4:
                clothing_item()
                break



