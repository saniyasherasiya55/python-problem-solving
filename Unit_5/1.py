# Program 41: Write a program to demonstrate different types of errors and exceptions in Python.
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Zero division error handled")

try:
    int("abc")
except ValueError:
    print("Value error handled")
