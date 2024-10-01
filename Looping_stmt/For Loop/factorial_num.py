# x = int(input("Enter the number:"))
# fact = 1
# for i in range(1,x+1):
#     fact = fact * i
# print(fact)

num = int(input("Enter the number:"))
fact = 1
if num<0:
    print("Please Enter the Positive value")
elif num==0:
    print("factorial of 0 is 1")
else:
    for x in range(1, num+1):
        fact *= x  # fact = fact * x
    print("Factorial of", num, "=", fact)