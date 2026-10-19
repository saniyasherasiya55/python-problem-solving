# Program 39: Write a program to read and write data into a file using different file modes.
with open("demo.txt", "w") as f:
    f.write("Hello Python")

with open("demo.txt", "r") as f:
    print(f.read())

with open("demo.txt", "a") as f:
    f.write(" Lab")
