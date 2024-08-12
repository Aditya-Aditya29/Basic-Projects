Flag=True

while Flag:
    print("----MENU----")
    print("1:- ADD")
    print("2:- SUB")
    print("3:- MULTIPLY")
    print("4:- DIVIDE")
    print("5:- Exit")

    user_input=int(input("Choose by number:-"))

    if user_input ==1:
        Num1 = int(input("Enter 1st number :-"))
        Num2 = int(input("Enter 2st number :-"))
        ans = Num1+Num2
        print("Sum of two number is "+ str(ans))

    elif user_input == 2:
        Num1 = int(input("Enter 1st number :-"))
        Num2 = int(input("Enter 2st number :-"))
        ans = Num1 - Num2
        print("Sub of two number is " +str(ans))

    elif user_input == 3:
        Num1 = int(input("Enter 1st number :-"))
        Num2 = int(input("Enter 2st number :-"))
        ans = Num1 * Num2
        print("Multiply of two number is " + str(ans))

    elif user_input == 4:
        Num1 = int(input("Enter 1st number :-"))
        Num2 = int(input("Enter 2st number :-"))
        ans = Num1 / Num2
        print("Division of two number is " + str(ans))

    elif user_input == 5:
        print("Exiting....!")
        Flag=False