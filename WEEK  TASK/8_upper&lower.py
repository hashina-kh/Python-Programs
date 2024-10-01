str1 = input("Enter a String  =")
lower = 0
upper = 0

for i in str1:
    if (i.islower()):
        lower+=1
    else:
        upper+=1
print("Lower is =",lower)
print("Upper is =",upper)