#Example of Privete Access Modifieres
class Student:
    def __init__(self,name, course, place):
        self.__Name = name
        self.__Course = course
        self.__Place = place

    def __display_data(self):
        print("Name    =",self.__Name)
        print("Place   =",self.__Place)
        print("Course  =",self.__Course)
    def Access_modifirs(self):
        self.__display_data()

obj = Student(name="HAshina",place="KAkanad",course="Python")
obj.Access_modifirs()

