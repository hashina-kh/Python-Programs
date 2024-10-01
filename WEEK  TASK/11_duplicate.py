list1 = [1,2,3,4,5,6,1,2,3]
result = []
# print(len(list1))
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j] and list1[i] not in result:
            result.append(list1[i])
print(result)