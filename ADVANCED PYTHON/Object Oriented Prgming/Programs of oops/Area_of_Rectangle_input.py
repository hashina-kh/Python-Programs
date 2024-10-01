class Rectangle:
    def __init__(self):
        self.Legth = ""
        self.Breadth = ""
    def input_area(self):
        self.Legth = float(input("Enter the Length:"))
        self.Breadth = float(input("Enter the Bredth:"))
    def display_Area(self):
        print("Area of Rectangle :",self.Legth*self.Breadth)

area = Rectangle()
area.input_area()
area.display_Area()