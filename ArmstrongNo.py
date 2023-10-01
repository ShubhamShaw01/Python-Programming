# write a code in python to check whether the no is armstrong or not
def isArmstrong(no):
    flag = no
    check = 0
    while (flag > 0):
        rem = flag % 10
        check += (rem*rem*rem)
        flag //= 10
    if (check == no):
        return True
    else:
        return False


if __name__ == "__main__":
    no = int(input("Enter the no to check whether : "))
    if (isArmstrong(no)):
        print(no, "is a armstrong no")
    else:
        print(no, "is not a armstrong no")
