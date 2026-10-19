# Program 42: Write a program to handle exceptions using try, except, else and finally blocks.
try:
    n = int("10")
except ValueError:
    print("Invalid number")
else:
    print("Number :", n)
finally:
    print("Program finished")
