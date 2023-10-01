#wap a program to check the no is perfect square or not 
def squareRoot(no):
    return (no**0.5)
if __name__=="__main__":
    no=int(input("Enter the no : "))
    result=squareRoot(no)
    if (result%1==0):
        print(f"{no} is perfect Square")
    else:
        print(f"{no} is not a perfect square is root is {result}")