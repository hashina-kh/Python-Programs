num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if (num1>num2):
    min=num1
else:
    min1=num2
while(1):
    if (min1%num1==0 and min1%num2==0):
       print("LCM is:", min1)
       break
    min1 = min1+1