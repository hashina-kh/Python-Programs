list1 = [1,2,3,4,5,6]
list2 = [4,5,3,2,6,7,8,9]
result = []
for i in list1:
    for j in list2:
        if i==j and i not in result:
            result.append(i)
print(result)