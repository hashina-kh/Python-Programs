list1 = [1,2,13,4,15,12,100,11,23,34]

max = list1[0]
# print(max)
for i in range(len(list1)):
    if list1[i] > max:
        max = list1[i]
print(max)