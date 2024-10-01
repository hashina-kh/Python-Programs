num = int(input("Enter 3 digit integer number ="))
temp = num
sum = 0

while num>0:
    digit = num%10
    sum += digit**3
    num//=10

if temp == sum:
    print("Is ArmStrong number")
else:
    print("Is not ArmStrong number")