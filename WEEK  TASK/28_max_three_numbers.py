num = int(input("Enter First number ="))
num1 = int(input("Enter Second number ="))
num2 = int(input("Enter Third number ="))

if num>num1 and num>num2:
    print("Largest number of",num)
elif num1>num and num1>num2:
    print("Largest number of",num1)
else:
    print("Largest number of",num2)