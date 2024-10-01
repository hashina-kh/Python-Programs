import re

mystring = "Indroduction to Regular Expression to in the python to programmming"

x = re.sub("\s", "_", mystring)

y = re.sub("to", ".", mystring)
print(x)
print(y)