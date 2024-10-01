num = int(input("Enter a number"))
fact = 1
if num<0:
    print("Please Enter a Positive Integer")
elif num==0:
    print("factorial of Zero is 1")
else:
    for i in range(1, num+1):
        fact *= i
    print(fact)