import re

mystring = "Indroduction to Regular Expression to in the python to programmming"

x = re.split("\s",mystring)
# or
# x = re.split(" ",mystring)

# x = re.split("to",mystring)


print(x)
print(type(x))