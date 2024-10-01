rows = int(input("Enter the number:"))
# Outer loop for handling the number of rows
for i in range(rows):
    # inner loop handling the number of columns
    for j in range(i+1):
        #Printing Stars
        print("*", end=" ")
    print()