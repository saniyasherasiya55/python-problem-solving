# Write a program to illustrate variable scope using local global and nonlocal variables. 


# Global Variable
x = 100

# Outer Function
def outer():

    # Local Variable
    y = 50

    # Inner Function
    def inner():

        # Nonlocal Variable
        nonlocal y

        # Modify local variable of outer function
        y = 75

        print("Inside Inner Function =", y)

    # Call inner function
    inner()

    print("Inside Outer Function =", y)

# Call outer function
outer()

# Print global variable
print("Global Variable =", x)



