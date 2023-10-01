#wap to find the area of rectangle use class 
class Rectangle:
    def __init__(self):
        self.length=0
        self.width=0
    def getData(self,x,y):
        self.length=x
        self.width=y
    def rectArea(self):
        return self.length*self.width

if __name__=="__main__":
    x = int(input("Enter the length of the Rectangle: "))
    y = int(input("Enter the breath of the Rectangle: "))
    rect=Rectangle()
    rect.getData(x,y)
    area=rect.rectArea()
    print(f"The area of the Rectangle is : {area}")

    