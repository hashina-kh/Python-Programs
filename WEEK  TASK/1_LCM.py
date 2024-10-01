#LCM
def calculate_lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while(True):
        if greater%x==0 and greater%y==0:
            lcm = greater
            break
        greater+=1
    return lcm

num = int(input("Enter first number of lcm ="))
num1 = int(input("Enter the Second number of lcm ="))

print(calculate_lcm(num,num1))

