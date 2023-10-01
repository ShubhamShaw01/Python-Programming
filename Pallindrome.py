# wap to find the no is pallindrome or not
def isPallindrome(no):
    flag = no
    check = 0
    while flag > 0:
        rem = flag % 10
        check = check*10+rem
        flag //= 10
    return check

if __name__=="__main__":
    no = int(input("Enter the no to check pallindrome or not : "))
    check=isPallindrome(no)
    if (check == no):
        print(f"{no} is pallindrome no ")
    else:
        print(f"{no}reverse is {check} so it is not a pallindrome no")
