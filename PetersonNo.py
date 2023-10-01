# write a code in python to check whether the no is peterson or not
def factorial(rem):
    check = 1
    if rem <= 1:
        return check
    else:
        for i in range(2, rem + 1):
            check *= i
        return check


def isPeterson(no):
    check = 0
    flag = no
    while flag > 0:
        rem = flag % 10
        fact = factorial(rem)
        check += fact
        flag //= 10

    return check


if __name__ == "__main__":
    no = int(input("Enter the number to check whether it's a Peterson number: "))
    result = isPeterson(no)

    if no == result:
        print(no, "is a Peterson number")
    else:
        print(no, "is not a Peterson number because digit factorial sum is ", result)
