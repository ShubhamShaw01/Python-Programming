# write a python program to find the factorial of the no
def factorial(no):
    fact = 1
    if no <= 1:
        print(f"{no}! = {fact}")
    else:
        for i in range(2, no + 1):
            fact *= i
        print(f"{no}! = {fact}")

if __name__ == "__main__":
    no = int(input("Enter the number to find its factorial: "))
    factorial(no)
