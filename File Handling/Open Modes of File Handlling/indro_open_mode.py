myfile = open("Demo.txt", "w")
myfile.write("Indrosuction to File Handling")
myfile.close()

x = open("Demo.txt", "r")
print(x.read())
x.close()

a = open("Demo.txt", "r")
print(a.read(10))