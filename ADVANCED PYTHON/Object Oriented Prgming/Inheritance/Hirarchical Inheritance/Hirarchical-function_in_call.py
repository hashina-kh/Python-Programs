class Hospital:
    def __init__(self):
        self.HospitalName = ""
        self.Location = ""
        self.Mobile = ""
    def Hospital_Data(self):
        print("---------PLEASE ENTER HOSPITAL DETAILS-----------")
        self.HospitalName = input("Enter Hospital Name          :")
        self.Location = input("Enter Hospital Location        :")
        self.Mobile = int(input("Enter Hospital Contact Number       :"))
    def Display_Hospital(self):
        print("---------------HOSPITAL DETAILS-----------------")
        print("HOSPITAL NAME             :",self.HospitalName)
        print("HOSPITAL LOCATION         :",self.Location)
        print("HOSPITAL CONTACT NUMBER   :",self.Mobile)

class Session(Hospital):
    def __init__(self):
        self.Session_Id = ""
        self.Session_Name = ""
        self.Doctor_Name = ""
    def Session_Data(self):
        obj.Hospital_Data()
        print("---------PLEASE ENTER SESSION DETAILS-----------")
        self.Session_Id = int(input("Enter the Session Id    :"))
        self.Session_Name = input("Enter the Session Name    :")
        self.Doctor_Name =  input("Enter the Doctor Name    :")
    def Display_Session(self):
        print()
        obj.Display_Hospital()
        print("---------------SESSION DETAILS-----------------")
        print("SESSION ID         :",self.Session_Id)
        print("SESSION NAME       :",self.Session_Name)
        print("DOCTOR NAME        :",self.Doctor_Name)
class Patient(Session):
    def __init__(self):
        self.Patient_Name = ""
        self.Patient_Age = ""
        self.Place = ""
        self.Gender = ""
        self.Contact  = ""
    def Patient_Data(self):
        print()
        obj.Session_Data()
        print("---------PLEASE ENTER PATIENT DETAILS-----------")
        self.Patient_Name = input("Enter the Patient Name    :")
        self.Patient_Age = int(input("Enter Patient Age      :"))
        self.Place = input("Enter Patient Location      :")
        self.Gender = input("Enter Patient Gender      :")
        self.Contact = int(input("Enter Patient Contact    :"))
    def Display_Patient(self):
        print()
        obj.Display_Session()
        print("---------------PATIENT DETAILS-----------------")
        print("PATIENT  NAME         :", self.Patient_Name)
        print("PATIENT AGE       :", self.Patient_Age)
        print("LOCATION       :", self.Place)
        print("GENDER       :", self.Gender)
        print("CONTACT NUMBER      :", self.Contact)

obj = Patient()
obj.Patient_Data()
obj.Display_Patient()


