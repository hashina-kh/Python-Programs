import re

mystring = "Indroduction to Regular Expression to in the python to programmming"

x = re.findall("to", mystring)
print(x)
print(len(x))