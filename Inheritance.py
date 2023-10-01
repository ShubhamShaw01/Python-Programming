#write a code in python for inheritances
class Bird:
    def __init__(self):
        self.message="chirping"
class Piegon(Bird):
    def __init__(self):
        super().__init__()
        self.message="Flying"
    def printMessage(self):
        b=Bird()
        print("Pigeon",self.message)
        print("Birds",b.message)
pc=Piegon()
pc.printMessage()