num = int(input("Enter the number  :"))
temp = num
sum = 0

while num>0:
    digit = num%10
    sum = sum +digit
    num//=10

if temp%sum==0:
    print("Is a Harshad number")
else:
    print("Is not Harshad numbwer")