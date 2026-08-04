# 10. Write a program to demonstrate recursion using factorial.

# Defining a recursive function to calculate factorial
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Call the function and display the result
print("Factorial of 6 is:", factorial(6))
