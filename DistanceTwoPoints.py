#write a code for finding the distance between two points 2d either 3d
import math
class Point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dist2D(self,other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
class Point3D(Point2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    def dist3D(self,other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z)** 2)
def main():
    choice=int(input("Enter 1 for 2d \nEnter 2 for 3d :"))
    if choice==1:
        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))
        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))
        point1=Point2D(x1,y1)
        point2=Point2D(x2,y2)
        distance=point1.dist2D(point2)
        print(f"Distance btween this two coordinates are : {distance}")
    elif choice==2:
        x1_3D = float(input("Enter the x-coordinate of the first point: "))
        y1_3D = float(input("Enter the y-coordinate of the first point: "))
        z1_3D = float(input("Enter the z-coordinate of the first point: "))
        x2_3D = float(input("Enter the x-coordinate of the second point: "))
        y2_3D = float(input("Enter the y-coordinate of the second point: "))
        z2_3D = float(input("Enter the z-coordinate of the second point: "))
        point1=Point3D(x1_3D,y1_3D,z1_3D)
        point2=Point3D(x2_3D,y2_3D,z2_3D)
        distance=point1.dist3D(point2)
        print(f"Distance btween this two coordinates are : {distance}")
    else:
        print("Wrong Choice")
if __name__=="__main__":
    main()