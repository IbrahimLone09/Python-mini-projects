# simple program for calculator

print("calculate whatever you like!")


while True:
    a ,b = int(input("Enter the first number: "))
    operator = input("Enter the operator (Q to Exit!): ")
    break
    b = int(input("Enter the second number: "))


    if operator == ("+"):
        print("sum is =", a + b)
        

    elif operator == ("-"):
        print("Difference is =",a - b)
        

    elif operator == ("*"):
        print("Multiplication is =", a * b)
        

    elif operator == ("/"):
        print("Division is =", a / b)
        
    else:
        print("Please enter the valid option!")