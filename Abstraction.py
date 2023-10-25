# Create an abstract class Shape with an abstract method calculateArea().
# Then, create two subclasses, Circle and Rectangle, which inherit from Shape and implement the calculateArea
# method to calculate the area of a circle and rectangle, respectively.
import math
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod 
    def calculteArea(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculteArea(self):
        return math.pi*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculteArea(self):
        return self.length*self.breadth

if __name__=="__main__":
    radius=int(input("Enter the radius of the circle : "))
    c = Circle(radius)
    circleArea=c.calculteArea()
    length=int(input("Enter the length of the rectangle : "))
    breadth=int(input("Enter the breadth of the rectangle :"))
    rec=Rectangle(length,breadth)
    rectangleArea=rec.calculteArea()
    print(f"Circle Area = {circleArea}")
    print(f"Rectangle Area = {rectangleArea}")