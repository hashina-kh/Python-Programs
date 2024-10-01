import os

# os.remove("text.txt.py")

if os.path.exists("hello.txt.py"):
    os.remove("hello.txt.py")
    print("Deleted")
else:
    print("File not Found..!")

#os.rmdir()
#os.mkdir("NewFoldeer")