#wap to check the no is perfect or not
def isPerfect(no):
    sum= 0
    for i in range(1,no):
        if no % i == 0:
            sum += i
    return sum

def main():
    no = int(input("Enter the number to check if it is a perfect number: "))
    result = isPerfect(no)
    if no == result:
        print(f"{no} is a perfect number.")
    else:
        print(f"{no} is not a perfect number, and the sum of its divisors is {result}.")

if __name__ == "__main__":
    main()
