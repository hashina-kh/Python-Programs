list1 = [9,8,5,6,7]
list2 = [1,2,3,4,5]

def addition(a,b):
    return a+b

c = list(map(addition, list1, list2))
print(c)