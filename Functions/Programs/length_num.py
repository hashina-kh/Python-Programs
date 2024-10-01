def calculate_length(n):
    length = 0
    while (n!=0):
        length+=1
        n//=10
    return length

num = int(input("Enter a number:"))
print("Length of given number:",calculate_length(num))