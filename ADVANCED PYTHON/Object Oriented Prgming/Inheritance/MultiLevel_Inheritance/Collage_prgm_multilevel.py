class Collage:
    def Collage_Details(self):
        self.Collage_Name = ""
        self.Location = ""
        self.Collage_Mobile = ""
    def Collage_data_input(self):
        print("__________PLEASE ENTER COLLAGE DETAILS__________")
        self.Collage_Name = input("Enter the Collage Name  :")
        self.Location = input("Enter Collage Location   :")
        self.Collage_Mobile = int(input("Enter Collage Contact Number   :"))
    def display_Collagedata(self):
        print("-----------Collage Details------------")
        print("COLLAGE NAME   :",self.Collage_Name)
        print("LOCATION       :",self.Location)
        print("COLLAGE CONTACT  :",self.Collage_Mobile)
class Depatment(Collage):
    def Depatment_Details(self):
        self.Dept_id = ""
        self.Dept_name = ""
        self.HOD_Name = ""
        self.Dept_Mobile = ""
    def Department_data_input(self):
        print("__________PLEASE ENTER Depatment DETAILS__________")
        self.Dept_id= int(input("Enter the Depatment ID  :"))
        self.Dept_name = input("Enter Department Name   :")
        self.HOD_Name = input("Enter HOD NAme   :")
        self.Dept_Mobile = int(input("Enter Department Contact :"))
    def display_Depat_data(self):
        print("-----------DEPARTMENT Details------------")
        print("DEPARTMENT ID  :",self.Dept_id)
        print("DEPARTMENT NAME   :",self.Dept_name)
        print("HOD NAME      :",self.HOD_Name)
        print("DEPARTMENT CONTACT  :",self.Dept_Mobile)

class Student(Depatment):
    def Student_Details(self):
        self.Stu_name = ""
        self.Stu_Age = ""
        self.Stu_Mobile = ""
        self.Stu_Email= ""
        self.Stu_Course = ""
        self.Stu_Place = ""

    def Student_data_input(self):
        print("__________PLEASE ENTER Student DETAILS__________")
        self.Stu_name= input("Enter the Student Name  :")
        self.Stu_Age = int(input("Enter Student Age   :"))
        self.Stu_Mobile = int(input("Enter Student Mobile   :"))
        self.Stu_Email = input("Enter Student Email :")
        self.Stu_Course = input("Enter Course :")
        self.Stu_Place = input("Enter Student Place  :")
    def display_Stu_data(self):
        print("-----------Student Details------------")
        print("STUDENT NAME :",self.Stu_name)
        print("STUDENT AGE   :",self.Stu_Age)
        print("STUDENT CONTACT :",self.Stu_Mobile)
        print("STUDENT EMAIL      :",self.Stu_Email)
        print("COURSE :",self.Stu_Course)
        print("LOCATION :",self.Stu_Place)

obj1 = Student()
obj1.Collage_data_input()
obj1.Department_data_input()
obj1.Student_data_input()

obj1.display_Collagedata()
obj1.display_Depat_data()
obj1.display_Stu_data()