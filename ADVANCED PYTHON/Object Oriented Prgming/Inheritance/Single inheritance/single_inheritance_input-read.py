class Collage:
    def Collage_details(self):
        self.Collage_Name = ""
        self.Location = ""
        self.Collage_Contact = ""
    def Collage_deatils_input(self):
        self.Collage_Name = input("Enter Collage Name   :")
        self.Location = input("Enter Location   :")
        self.Collage_Contact = int(input("Enter Contact Number   :"))
    def dispay_collage(self):
        print("_______________PLEACE ENTER COLLAGE DETAILS____________________")
        print("Collage Name       :",self.Collage_Name)
        print("Collage Location   :",self.Location)
        print("Collage Contact    :",self.Collage_Contact)
class Department(Collage):
    def Department_details(self):
        self.Dept_Id = ""
        self.Dept_Name = ""
        self.HOD_Name = ""
        self.Dept_Contact = ""
    def Depatment_details_input(self):
        print("_______________PLEACE ENTER DEPARTMENT DETAILS____________________")
        self.Dept_Id = int(input("Enter Depatment Id  :"))
        self.Dept_Name = input("Enter Department Name  :")
        self.HOD_Name = input("Enter HOD Name   :")
        self.Dept_Contact = int(input("Enter Depatment Mobile  :"))
    def dispay_depart(self):

        print("Department ID   :",self.Dept_Id)
        print("Department Name :",self.Dept_Name)
        print("HOD Name        :",self.HOD_Name)
        print("Department Contact  :",self.Dept_Contact)
obj1 = Department()
obj1.Collage_deatils_input()
obj1.Depatment_details_input()

obj1.dispay_collage()
obj1.dispay_depart()