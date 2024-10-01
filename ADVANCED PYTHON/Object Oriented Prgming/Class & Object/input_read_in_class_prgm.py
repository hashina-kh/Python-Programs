class inputRead:
    def __init__(self):
        self.Name = ""
        self.Place = ""
        self.Age = ""
    def get_input_data(self):
        self.Name = input("Enter Your Name :")
        self.Place = input("Enter Your Location :")
        self.Age = int(input("Enter Your Age:"))
    def display_input_data(self):
        print("----------DETAILS--------")
        print("Name :",self.Name)
        print("Location  :",self.Place)
        print("Age    :",self.Age)

obj1 = inputRead()
obj2 = inputRead()


obj1.get_input_data()
print()
obj1.display_input_data()

print()      #Edayil Space idan   eg:- (enter key space)
obj2.get_input_data()
obj2.display_input_data()
