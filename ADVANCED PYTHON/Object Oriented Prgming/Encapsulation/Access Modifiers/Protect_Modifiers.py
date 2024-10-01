#Example of Protected Access Modifiers
class Student:
    def __init__(self,name, roll_no, place):
        self._Name = name
        self._roll_no = roll_no
        self._place = place
    def _display(self):
        print("Roll_number  =",self._roll_no)
        print("Place        =",self._place)
class Newclass(Student):
    def __init__(self,name, roll_no, place):
        Student.__init__(self,name, roll_no, place)
    def display_data(self):
        print("NAme   =",self._Name)
        self._display()

obj = Newclass("HAshina",1,"Kakkanad")
obj.display_data()
