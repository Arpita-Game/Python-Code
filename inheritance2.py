class Car:
    def start(self):
        print("Car has started")

    def stop(self):
        print("Car is stopped")


class ToyotaCar(Car):
    def type(self):
        print("ev")
    

class Carlook(ToyotaCar):
    def color(self):
        print("White")


car1 =Car()
car1.start()
t1=ToyotaCar()
t1.type()
t1.stop()
cl=Carlook()
cl.color()
cl.type()
cl.stop()