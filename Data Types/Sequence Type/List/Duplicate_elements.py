# python Programs to print the duplicate Elements
mylist = [1,2,3,4,5,57,56,8,1,2,5,57]
# print(len(mylist))
result =[]
for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        if mylist[i] == mylist[j] and mylist[i] not in result:
            result.append(mylist[i])
print(result)