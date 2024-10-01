num = int(input("Enter a number:"))
if num == 1:
    print("1 is not prime number")
elif num == 0:
    print("You've Entered Zero")
elif num<0:
    print("Please Enter a Positive number")
else:
    for i in range(2, num):
        if num % i == 0:    # prime number is 1 , kodukunna number um kond mathram divide cheyyumbol riminder 0 avanunna number
            print("number is not prime")
            break
    else:
        print("is a prime number")