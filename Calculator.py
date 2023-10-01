# write a python program for calculator
while True:
    no1 = int(input("Enter the 1st no : "))
    no2 = int(input("Enter the 2nd no : "))
    operation = int(input("Enter \n1 for addition, \n2 for subtraction, \n3 for multiplication, \n4 for division: "))

    if operation == 1:
        print(f"The sum of {no1} and {no2} = {no1 + no2}")
    elif operation == 2:
        print(f"The subtraction of {no1} and {no2} = {no1 - no2}")
    elif operation == 3:
        print(f"The product of {no1} and {no2} = {no1 * no2}")
    elif operation == 4:
        if no2 != 0:
            div = no1 / no2
            print(f"The division of {no1} and {no2} = {div:.2f}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("You gave a wrong input!")

    check = input("Enter 'y' or 'yes' to continue: ").lower()
    if check not in ('y', 'yes'):
        break
