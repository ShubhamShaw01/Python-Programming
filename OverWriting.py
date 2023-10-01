#wap to print test overwriting
class OverWrite:
    def showMessage(self, a=None, b=None):
        if a is None and b is None:
            print("This is class a")
        else:
            print("The sum of the numbers is:", a + b)
        
if __name__=="__main__":
    OverWrite().showMessage()
    OverWrite().showMessage(5,6)