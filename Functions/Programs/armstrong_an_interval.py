start = int(input("Enter the First number:"))
end = int(input("Enter the Second number:"))

for num in range(start, end + 1):
    length = len(str(num))

    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10

    if num == sum:
        print(num)