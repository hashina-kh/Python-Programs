class Employee:
    def __init__(self,name,mobile,email,company,salary,location):
        self.Employee_Name = name
        self.Employee_Contact = mobile
        self.Employee_Email = email
        self.Employee_Company = company
        self.Employee_Salary = salary
        self.Employee_Place = location

    def Employee_Details(self):
        print("----------EMPLOYEE DETAILS-----------")
        print("Name   :",self.Employee_Name)
        print("Contact   :",self.Employee_Contact)
        print("Email  :",self.Employee_Email)
        print("Company   :",self.Employee_Company)
        print("Salary   :",self.Employee_Salary)
        print("Place   :",self.Employee_Place)

emp1 = Employee("Anna",1234567890,"Anna2@gmail.com","TCS",200000,"Kottayam")
emp2 = Employee("Abin",1234512345,"abin2@gmail.com","Google",10000000,"Alapuzha")
emp3 = Employee("Alen",2345612789,"alen@gmail.com","Accenture",3000000,"Kochi")

emp1.Employee_Details()
emp2.Employee_Details()
emp3.Employee_Details()