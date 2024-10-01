try:
    x = int(input("Enter the First number:"))
    y = int(input("Enter the Second number:"))
    result = x/y
    print(result)
except ZeroDivisionError:               # Exception Clause with Exception
    print("Error Occured...")


# Exception Clause With no exception
except:
    print("Error Occured...!")
