#to implement multiple inheritances
class Vehicle:
    def start(self):
        pass
    def stop(self):
        pass
class Music:
    def playMusic(self):
        pass
    def changeTrack(self):
        pass
class Car(Vehicle, Music):
    def start(self):
        print("Start the car")
    def stop(self):
        print("Stop the car")
    def playMusic(self):
        print("Play song")
    def changeTrack(self):
        print("Change Song")
if __name__=="__main__":
    car=Car()
    car.start()
    car.playMusic()
    car.changeTrack()
    car.stop()