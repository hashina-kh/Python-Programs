class A:
    def function_A(self):
        print("Inside Class A")
class B(A):
    def function_B(self):
        print("Inside Class B")
class C(B):
    def function_C(self):
        print("Inside Class C")

obj1 = C()
obj1.function_A()
obj1.function_B()
obj1.function_C()