#using insert() method
x = ["Anna", "Abin", 1234, 5673, [1,2,3,4,5]]
x.insert(0, "Libina")
print(x)

list1 = ["Mango", "Orange", "Apple"]
list2 = ["Pinapple", "Aplle","Tomato"]
list1.insert(1, list2)
print(list1)

#Using Append() method            auto add  last position
a = ["Mango", "Apple", "Pinapple","orange"]
b = ["Onion", "Tomattoi", "Chilli"]
a.append(b)
print(a)


#Using Extend method             orumich 1 list agum
x1 = ["Mango", "Apple", "Pinapple","orange"]
y1 = ["Onion", "Tomattoi", "Chilli"]
x1.extend(y1)
print(x1)

#Using + Operator
x2 = ["Mango", "Apple", "Pinapple","orange"]
y2 = ["Onion", "Tomattoi", "Chilli"]
# Using + Operator
print(x2+y2)