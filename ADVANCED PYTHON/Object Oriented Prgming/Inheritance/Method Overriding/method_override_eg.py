class Birds:
    def function1(self):
        print("There are multiple types of birds....!")
    def flight1(self):
        print("Many these birds in fly but some birds cannot fly..!")
class Sparrow(Birds):
    def flight1(self):
        print("Sparrow are Birds which can fly")
class Ostrich(Birds):
    def flight1(self):
        print("Ostrich are the birds which cannot fly")

obj1 = Birds()
obj1.function1()
obj1.flight1()

obj = Sparrow()
obj.function1()
obj.flight1()   # overriding the Parent class same function

obj2 = Ostrich()
obj2.flight1()