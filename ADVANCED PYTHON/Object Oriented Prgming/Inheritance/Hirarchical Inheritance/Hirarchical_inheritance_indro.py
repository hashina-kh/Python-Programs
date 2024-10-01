class A:
    def function_A(self):
        print("Inside Parent Class A")
class B(A):
    def function_B(self):
        print("Inside Child Class B")
class C(A):
    def function_C(self):
        print("Inside Child class C")
class D(A):
    def function_D(self):
        print("Inside Child Class D")
obj = B()
obj.function_A()
obj.function_B()

obj1 = C()
obj1.function_A()
obj1.function_C()

obj2 = D()
obj2.function_A()
obj2.function_D()