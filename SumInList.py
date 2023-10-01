# Write a program to calculate the sum of all the numbers in a list
def SumInList(n):
    l = []
    for i in range(n):
        l.append(int(input(f"Enter the {i+1} Element : ")))
    sum = 0
    for i in l:
        sum += i
    print("Sum of the element of the list is :", sum)


n = int(input("Enter the length of the list you wnat to enter : "))
SumInList(n)
