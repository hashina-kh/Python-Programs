
#Example of Public Access Modifiers
class Student:
    def __init__(self, name, course):
        #Public Data Members
        self.Name = name
        self.Course = course

    #public Member Function
    def display_data(self):
        print("------Student Details---------")
        print("Name   =", self.Name)
        print("Corse  =",self.Course)

obj = Student("Hashina", "Python")
obj.display_data()
