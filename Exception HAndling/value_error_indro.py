try:
    x = int(input("Enter the First number:"))
    y = int(input("Enter the Second number:"))
    result = x/y
    print(result)
except ZeroDivisionError:
    print("Error Occured....!")
except ValueError:
    print("Value Error.....!")