#HCF (highest Common Factor)
def calculate_HCF(x,y):
    if x>y:
        smallest = y
    else:
        smallest = x

    for i in range(1,smallest+1):
        if x%i==0 and y%i==0:
            hcf = i
    return hcf

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

print("HCF is =",calculate_HCF(num1,num2))