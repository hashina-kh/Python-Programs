num = int(input("Enter the number:"))
temp = num
sum = 0
if num<=0:
    print("Please Entered Positive number")
else:
    while num>0:
        sum += num
        num -= 1  # next value edukan
    print("Sum of ",temp, "Natural number =", sum)