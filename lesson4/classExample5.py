# coding=utf-8
# example polymophism
class Car:
    def __init__(self,brand,model):

        self.brand=brand
        self.model=model
    def move(self):
        print("Car, I am driving")    
class Boat:
    def __init__(self,brand,model):

        self.brand=brand
        self.model=model
    def move(self):
        print("Boat I am Sailing")
class Plane:
    def __init__(self,brand,model):

        self.brand=brand
        self.model=model
    def move(self):
        print("Plane ,I am Flying") 

car1=Car("Ford","Mustang")
boat1=Boat("Ibiza","Touring 200")
plane1=Plane("Boeing","777")
for x in(car1,boat1,plane1):
    x.move()

    
        