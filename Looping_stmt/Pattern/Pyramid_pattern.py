rows = int(input("Enter the number:"))
# space = 2*rows   increment starting space
space = rows
for i in range(rows):
    for s in range(space):
        print(end=" ")    # starting space
    space = space-1     # decrement space
    for j in range(i+1):    # column
        print("*", end=" ")   # space btween *
    print()