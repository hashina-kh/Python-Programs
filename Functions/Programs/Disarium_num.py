def calculate_length(n):
    length = 0
    while(n!=0):
        length+=1
        n //= 10
    return length
num = int(input("Enter a number:"))
# print(calculate_length(num))

# Disarium Number

len = calculate_length(num)

sum = 0
rem = 0
temp = num
while num>0:
    rem = num%10
    sum = sum + (rem**len)
    num //= 10
    len -= 1

if sum==temp:
    print("Is a Disarium Number")
else:
    print("is not Disarium")


