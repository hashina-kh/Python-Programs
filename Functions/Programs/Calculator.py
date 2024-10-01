def addition(x, y):
    return x+y

def substraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def divition(x,y):
    return x/y

print("----------- PLEASE SELECT YOUR CHOICE --------------")

print("A    Addition")
print("B    Substraction")
print("C    Multiplication")
print("D    Divition")

choice = (input("Enter Your Choice:"))
if choice in ('A','a','B','b','C','c','D','d'):

    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the Second number:"))

    if choice == "A" or choice == "a":
        print("Sum  =", addition(num1, num2))

    elif choice == "B" or choice == "b":
        print("Difference =", substraction(num1, num2))

    elif choice == "C" or choice == "c":
        print("Product  =", multiplication(num1, num2))

    elif choice == "D" or choice == "d":
        print("Division  =", divition(num1, num2))

else:
    print("Invalid Choice")
