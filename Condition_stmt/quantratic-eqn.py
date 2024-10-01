from math import sqrt
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))

root = (b ** 2) - (4 * a * c)

if root > 0:
    x1 = (-b + sqrt(root)) / (2 * a)
    x2 = (-b - sqrt(root)) / (2 * a)
    print("Two result are", x1, "and", x2)

elif root == 0:
    x3 = (-b) / (2 * a)
    print("result is", x3)

else:
    print("There is no roots discriminant less than 0")

