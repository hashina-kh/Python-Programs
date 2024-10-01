class A:
    def function_A(self):
        print("Inside A class")
class B:
    def function_B(self):
        print("Inside B class")
class C(A,B):
    def function_C(self):
        print("Inside C class")

obj1 = C()
obj1.function_A()
obj1.function_B()
obj1.function_C()