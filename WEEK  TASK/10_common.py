list1 = [1,2,3,4,5]
list2 = [8,9,0,7,1,2]

list3 = []
for i in list1:
    for j in list2:
        if i == j and i not in list3:
            list3.append(i)
print(list3)


