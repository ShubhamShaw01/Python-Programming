#wap to print the volume of cube and cuboid
class CuboidOrCube:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height
    def calculateVolume(self):
        return self.length*self.width*self.height
if __name__=="__main__":
    choice=int(input("Enter 1 for cube \nEnter any other no for cuboid : "))
    if choice==1:
        length=int(input("enter the edge length of cube : "))
        c=CuboidOrCube(length,length,length)
        resultVolume=c.calculateVolume()
        print(f"The volume of cube is {resultVolume}")
    else:
        length=int(input("enter the edge length of cuboid : "))
        width=int(input("enter the edge width of cuboid : "))
        height=int(input("enter the edge height of cuboid : "))
        c=CuboidOrCube(length,width,height)
        resultVolume=c.calculateVolume()
        print(f"The volume of cube is {resultVolume}")