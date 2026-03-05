start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))


def even():
    print("The even numbers will be:")
    for num in range(start_num,end_num + 1):
        if num > 1 and num % 2 == 0:
           print(num)



def odd():
    print("The odd numbers will be:")
    for num in range(start_num,end_num + 1):
        if num >= 1 and num % 2 != 0:
            print(num)


def prime():
    print("The prime numbers will be:")
    for num in range(start_num,end_num + 1):
     if num > 1:
        for i in range(2,int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


def whole():
    print("The whole numbers will be:")
    for num in range(start_num,end_num + 1):
        if num >= 0:
            print(num)


def composite():
    print("The composite numbers will be:")
    for num in range(start_num,end_num + 1):
        for i in range(2,int(num ** 0.5) + 1):
            if num % i == 0:
                print(num)


def natural():
    print("The natural numbers will be:")
    for  num in range(start_num,end_num + 1):
        if num >= 1:
            print(num)



while True:
    choice = input("Which numbers you would like to print,TYPE(prime,odd,even etc...) (Q to quit!): ").lower()
    if choice == "q":
        break
    elif choice == "even":
        even()
        
       
    elif choice == "prime":
        prime()
        

    elif choice == "odd":
        odd()
       

    elif choice == "whole":
        whole()
       

    elif choice == "composite":
        composite()
        

    elif choice == "natural":
        natural()
      

    else:
        print("Next time please choose from the above options!")
      