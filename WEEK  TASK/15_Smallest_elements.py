list1 = [13,4,15,12,100,11,23,34]
min = list1[0]
# print(min)

for i in range(len(list1)):
    if list1[i] < min:
        min = list1[i]
print(min)