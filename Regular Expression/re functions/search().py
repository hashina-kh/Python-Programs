import re

mystring = "Indroduction to Regular Expression to in the python to programmming"

x = re.search("\s", mystring)

print(x)
print(x.start())
print(x.end())