# x = 20
# y = 10
x = int(input("Enter first number:"))
y = int(input("Enter Second number:"))

print("Before swapping x = ", x)
print("Before swapping y = ", y)
x -= y   # x = x-y
y += x   # y = y+x
x = y - x
print("After swapping x =", x)
print("After swapping y =", y)
