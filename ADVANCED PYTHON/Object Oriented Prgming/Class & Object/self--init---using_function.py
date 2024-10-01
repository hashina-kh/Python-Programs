class myclass:
    def __init__(self,name,age):
        self.student_name = name
        self.Age = age
    def display(self):
        print("Name :", self.student_name)
        print("Age :", self.Age)

objname = myclass("Hashina",21)
objname.display()

objname1 = myclass("Anna",23)
objname1.display()

