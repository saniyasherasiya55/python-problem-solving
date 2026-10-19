# Program 43: Write a program to define and raise user-defined exceptions.
class AgeError(Exception):
    pass

age = 16
try:
    if age < 18:
        raise AgeError("Age must be 18 or above")
except AgeError as e:
    print(e)
