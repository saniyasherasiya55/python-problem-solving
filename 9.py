# 9. Write a program to define and use user-defined functions with different types of arguments.

# Define a user-defined function
def add(a, b):
    return a + b

# Call the function using positional arguments
print("Addition of 5 and 3 is:", add(5, 3))

# Call the function using keyword arguments
print("Addition of 10 and 20 is:", add(a=10, b=20))
