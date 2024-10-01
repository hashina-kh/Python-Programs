# Delete method 2 types

set1 = {"Ashika","Anna","Abin","Vishnu"}
print(set1)

# remove()
set1.remove("Vishnu")
print(set1)

# set1.remove("Python")
# print(set1)                  error

# discard()
set1.discard("Anna")
print(set1)

# set1.remove("Python")
# print(set1)                 no error --- no change
# Pop()
set1.pop()
print(set1)