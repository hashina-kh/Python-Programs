num = int(input("Enter the 3 digit of Number:"))
sum = 0
temp = num

while temp>0:
    digit = temp%10   # digit seperate cheyyan
    sum += digit**3    # sum = sum + digit**3
    temp //= 10        # temp = temp // 10  (temp Balance edukan)

if sum == num:
    print(sum, "Is a Armstrong Number")
else:
    print("Is not a Armstrong Number")