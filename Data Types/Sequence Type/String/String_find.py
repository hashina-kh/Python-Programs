x = "Welcome to luminar technolab....! to"
print(x.count("to"))
print("-----------------Function to find a string in python-------------------")
print("Using find() method    :", x.find("to"))
print("Using find() method    :", x.find("Python"))

print("Using index() method   :", x.index("luminar"))
# print("Using index() method   :", x.index("Python"))

print("Using rfind() method    :", x.rfind("to"))
print("Using rfind() method result=   :", x.rfind("to", 0, 30))

y = "Luminar"
print(x.rfind(y))