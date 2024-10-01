def reverse_string(n):
    rev = ""
    for i in n:
       rev = i + rev
    return rev

string = input("Enter a String =")

print(reverse_string(string))