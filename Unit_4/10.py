# Program 40: Write a program to perform file pointer operations using seek and tell methods.
with open("sample.txt", "w+") as f:
    f.write("Python")
    print("Position :", f.tell())
    f.seek(0)
    print("After seek :", f.tell())
    print("Text :", f.read())
