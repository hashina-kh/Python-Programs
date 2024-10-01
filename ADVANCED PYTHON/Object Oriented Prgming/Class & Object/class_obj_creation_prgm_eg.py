class Student:
    def __init__(self,name,age,place,course,mobile):
        self.Student_name = name
        self.Student_age = age
        self.Student_location = place
        self.Student_course = course
        self.Student_contact = mobile

    def display_data(self):
        print("----------------Student Details----------------")
        print("Name     :",self.Student_name)
        print("Age      :",self.Student_age)
        print("Place    :",self.Student_location)
        print("Course   :",self.Student_course)
        print("Phone    :",self.Student_contact)

obj1 = Student("Anna",23,"Kottayam","Python Django",1234567890)
obj1.display_data()

obj1 = Student(age=21,course="Python Flask",mobile=1234567123,name="Abin",place="Alapuzha")
obj1.display_data()
