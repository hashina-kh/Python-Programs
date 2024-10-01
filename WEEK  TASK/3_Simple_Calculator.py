print("Simple Calculator")
print("1: Adding")
print("2: SubStraction")
print("3: Multiply")
print("4: Divide")

choice = input("Enter the choice  ('1','2','3','4')")

if choice in ('1','2','3','4'):
    num1 = int(input("Enter First value:"))
    num2 = int(input("Enter Second Value:"))

    if choice == '1':
        print("Addition is:",num1 + num2)
    elif choice == '2':
        print("Substraction of", num1, "and", num2, "is :", num1-num2)
    elif choice == '3':
        print("Multiply of", num1, "and", num2, "is :", num1*num2)
    elif choice == '4':
        print("Divided by of", num1, "and", num2, "is :", num1//num2)
else:
    print("Please choose the any number!")
