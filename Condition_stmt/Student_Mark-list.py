physics = float(input("Enter the Mark for Physics   :"))
chemistry = float(input("Enter the Mark for Chemistry   :"))
biology = float(input("Enter the Mark for Biology   :"))
maths = float(input("Enter the Mark for maths   :"))
computer = float(input("Enter the Mark for Computer   :"))
Total = physics+chemistry+biology+maths+computer
print("Total marks Out of 500   =", Total)
percentage = (Total/500)*100
print("Percentage  =", percentage, "%")

if percentage>=90:
    print("A Grade")
elif percentage>=80:
    print("B Grade")
elif percentage>=70:
    print("C Grade")
elif percentage>=60:
    print("D Grade")
else:
    print("Failed")

