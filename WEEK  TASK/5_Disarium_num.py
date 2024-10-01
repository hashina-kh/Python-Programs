def calculate_length(n):
    length = 0
    while(n!=0):
        length+=1
        n//=10
    return length

num = int(input("Enter a number ="))

# print(calculate_length(num))

lengt = calculate_length(num)

sum = 0
temp = num
rem = 0

while num>0:
    rem = num%10
    sum = sum+ (rem**lengt)
    num//=10
    lengt-=1
if temp==sum:
    print("IS disarium number")
else:
    print("Is not a Diasrium number")


