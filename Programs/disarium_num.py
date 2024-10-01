num = int(input("Enter the number:"))
temp = num
y = str(num)
i = len(y)

result = 0
while temp>0:
    digit = temp % 10
    result += (digit ** 1)
    temp = temp//10
    i=i-1
print(result)
if result == num:
    print("number is disarium")
else:
    print("number is not disarium")




