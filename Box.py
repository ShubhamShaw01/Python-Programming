#Calculate the volume of a box by using overriding construct user can put 3 different values say some values on no values
class Box:
    def __init__(self,length=1,width=1,height=1):
        self.length=length
        self.width=width
        self.height=height
    def calculateVolume(self):
        return self.length*self.width*self.height
if __name__=="__main__":
    b=Box()
    choice = int(input("Enter how many input values you want to provide (0 to 3): "))
    if choice==0:
        result=b.calculateVolume()
        print(f"Volume is : {result}")
    elif choice==1:
        length=int(input("Enter the length : "))
        b=Box(length)
        result=b.calculateVolume()
        print(f"Volume is : {result}")
    elif choice==2:
        length=int(input("Enter the length : "))
        width=int(input("Enter the width : "))
        b=Box(length,width)
        result=b.calculateVolume()
        print(f"Volume is : {result}")
    elif choice==3:
        length=int(input("Enter the length : "))
        width=int(input("Enter the width : "))
        height=int(input("Enter the height : "))
        b=Box(length,width,height)
        result=b.calculateVolume()
        print(f"Volume is : {result}")
    else:
        print("Invalid Input!")
        