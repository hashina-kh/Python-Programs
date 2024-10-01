mylist = [1,2,3,4,5,57,56,8,1,2,5,100]
print(len(mylist))
max = mylist[0]

for i in range(len(mylist)):
    if mylist[i]>max:
        max = mylist[i]

print(max)
