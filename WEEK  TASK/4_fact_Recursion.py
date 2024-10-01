def calculate_fact(n):
    if n==1:
        return n
    else:
        return n*calculate_fact(n-1)
num = int(input("Emter a number  ="))

if num==0:
    print("Factorial of 0 is 1")
elif num<0:
    print("Please Enter the Positive number")
else:
    print("Factorial is =",calculate_fact(num))