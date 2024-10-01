num1 = 0
num2 = 1

x = int(input("Enter a limit:"))

print(num1)
print(num2)

for i in range(3, x+1):
    sum = num1+num2
    num1 = num2
    num2 = sum
    print(sum)

