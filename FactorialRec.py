#write a python program to write the factorial of the user given no
def factorial(no):
    if no <= 1:
        return 1
    else:
        return no * factorial(no - 1)

if __name__ == "__main__":
    no = int(input("Enter the number to find its factorial: "))
    result = factorial(no)
    print(f"{no}! = {result}")
