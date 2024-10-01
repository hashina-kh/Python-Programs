#LCM (Least Common Multiply)
def calculate_LCM(x,y):
    if x>y:
        greater = x
    else:
        greater = y

    while(True):
        if greater%x==0 and greater%y==0:
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

print("LCM is",calculate_LCM(num1,num2))