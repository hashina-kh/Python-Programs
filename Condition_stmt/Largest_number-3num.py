num = int(input("Enter first number:"))
num1 = int(input("Enter second number:"))
num2 = int(input("Enter third number:"))
if num>num1 and num>num2:
    print("Largest number is",num)
elif num1>num2 and num1>num:
    print("Largest number is", num1)
else:
    print("Largest number is", num2)
