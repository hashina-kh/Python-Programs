class Person:
    def __init__(self):
        self.per_name = ""
        self.per_age = ""
    def Personal_deatails(self):
        print("_______PLESE ENTER PERSON DETAILS__________")
        self.per_name = input("Enter the Person Name         :")
        self.per_age = int(input("Enter the Person Age        :"))
    def dispay_Person_data(self):
        print("___________PERSON DETAILS___________")
        print("Name      :",self.per_name)
        print("Age       :",self.per_age)
class Company:
    def __init__(self):
        self.Company_name = ""
        self.Location = ""
        self.Contact = ""
    def Company_details(self):
        print("_______PLESE ENTER COMPANY DETAILS__________")
        self.Company_name = input("Enter the Company Nmae    :")
        self.Location = input("Enter the Company Location    :")
        self.Contact = input("Enter the Company Contact :")
    def display_Company_data(self):
        print("___________PERSON DETAILS___________")
        print("Company Name       :",self.Company_name)
        print("Location           :",self.Location)
        print("Contact            :",self.Contact)
class Employee(Person,Company):
    def __init__(self):
        self.Designation = ""
        self.salary = ""
        self.skill = ""
        self.gender = ""

    def Employee_details(self):
        print("_______PLESE ENTER EMPLOYEE DETAILS__________")
        self.Designation = input("Enter the Designation   :")
        self.salary = int(input("Enter the Salary    :"))
        self.skill = input("Enter the Skill :")
        self.gender = input("Enter the Gender :")
    def dispay_Employee_data(self):
        print("________EMPLOYEE DETAILS__________")
        print("Designation      :",self.Designation)
        print("Salary           :",self.salary)
        print("Skills           :",self.skill)
        print("Gender          :",self.gender)

obj = Employee()
obj.Personal_deatails()
obj.Employee_details()
obj.Company_details()

obj.dispay_Person_data()
obj.dispay_Employee_data()
obj.display_Company_data()

