#wap to check the user give no is Perfect cube or not
import math
def cubeRoot(no):
    return math.cbrt(no)

if __name__=="__main__":
    no=int(input("Enter the no : "))
    result=cubeRoot(no)
    if (result%1==0):
        print(f"{no} is cube Square")
    else:
        print(f"{no} is not a cube square is root is {result}")
