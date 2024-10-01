def factorial_Recursion(n):
    if n==1:
        return n
    else:
        return n*factorial_Recursion(n-1)
num = int(input("Enter the number:"))
if num<0:
    print("Please Enter a Positive number")
elif num==0:
    print("Factorial of Zero is 1")
else:
    print("Factorial is:", factorial_Recursion(num))