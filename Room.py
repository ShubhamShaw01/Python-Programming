#calculate the area and volume of the room by using single inheritance
class RoomArea:
    def __init__(self):
        self.length = 0
        self.width = 0

    def getData(self, x, y):
        self.length = x
        self.width = y

    def Area(self):
        return self.length * self.width

class RoomVolume(RoomArea):
    def __init__(self):
        super().__init__() 
        self.height = 0

    def getData(self, x, y, z):
        super().getData(x, y)
        self.height = z

    def volume(self):
        return self.length * self.width * self.height

if __name__ == "__main__":
    x = int(input("Enter the length of the room : "))
    y = int(input("Enter the width of the room : "))
    z = int(input("Enter the height of the room : "))
    a = RoomVolume()
    a.getData(x, y, z)
    area = a.Area()
    volume = a.volume()
    print(f"Area of the room = {area}")
    print(f"Volume of the room = {volume}")
