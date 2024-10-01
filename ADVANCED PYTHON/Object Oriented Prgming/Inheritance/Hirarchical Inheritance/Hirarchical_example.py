class vehicle:
    def info(self):
        print("-----Vehicles-------")
class Car(vehicle):
    def car_info(self):
        print("Cars are difference brands like Maruthi Zusugi, Toyatto, BMW, Benzz")
class Trucker(vehicle):
    def Trucker_info(self):
        print("Trucker are Lori etc")
class Bike(vehicle):
    def Bike_info(self):
        print("Bikes are Yamaha, R15, Radion, BMW etc")

obj = Car()
obj.info()
obj.car_info()

obj1 = Trucker()
obj1.info()
obj1.Trucker_info()

obj2 = Bike()
obj2.info()
obj2.Bike_info()