start = int(input("Enter Start number ="))
End = int(input("Enter end number ="))


for i in range(start,End+1):
    length = len(str(i))
    sum = 0
    temp = i

    while temp>0:
        digit = temp%10
        sum = sum + digit ** length
        temp//=10

        if i == sum:
            print(i)

