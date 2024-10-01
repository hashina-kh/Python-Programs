#HCF (highest Common Factor)

def calculate_hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    
    for i in range(1, smaller+1):
        if x%i==0 and y%i==0:
            hcf = i
    return hcf
num = int(input("Enter first number :"))
num1 = int(input("Enter Second  number :"))

print("HCF is =",calculate_hcf(num,num1))

            