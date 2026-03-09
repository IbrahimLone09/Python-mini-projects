# simple program for calculator

print("calculate whatever you like!")

a = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
b = int(input("Enter the second number: "))

while True:
    if operator == ("+"):
        print("sum is =", a + b)
        break

    elif operator == ("-"):
        print("Difference is =",a - b)
        break

    elif operator == ("*"):
        print("Multiplication is =", a * b)
        break

    elif operator == ("/"):
        print("Division is =", a / b)
        break