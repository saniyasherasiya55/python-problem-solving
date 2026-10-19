# Program 32: Write a program to demonstrate constructor and destructor usage.
class Demo:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")

obj = Demo()
del obj
