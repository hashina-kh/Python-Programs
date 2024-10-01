class Rectangle:
    def __init__(self,length,breadth):
        self.Length = length
        self.Breadth = breadth

    def display_data(self):
        print("Area of Rectangle  :", self.Length*self.Breadth)

obj1 = Rectangle(10,5)
obj1.display_data()