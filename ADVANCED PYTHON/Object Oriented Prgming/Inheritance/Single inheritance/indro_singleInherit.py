class collage:
    def collage_function(self):
        print("Inside of collage function")

class department(collage):
    def depatment_function(self):
        print("Inside of Depatment functions")

obj1 = department()
obj1.collage_function()
obj1.depatment_function()