def calculate_digit(n):
    digit = 0
    while (n!=0):
        digit+=1
        n//=10
    return digit
num = int(input("Enter integer number ="))
print(calculate_digit(num))