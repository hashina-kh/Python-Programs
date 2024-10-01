class Car:
    def __init__(self, name, price, colour):
        self.Name = name
        self.Price = price
        self.colour = colour

    def start(self):
        print(self.Name + "Engine Started")

car1 = Car("Maruthi", 200000, "red")
car2 = Car("Toyotta", 100000, "White")
#price change akkan
car1.Price = 500000

# color delete akkan
del car1.colour

print(car1.Name, car1.Price)
print(car2.Name, car2.Price, car2.colour)


car1.start()
