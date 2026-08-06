# 3. Write a program to generate a multiplication table using a for loop.


num = int(input("Enter a number: "))

# Using for loop to print multiplication table
for i in range(1, 11):


    print(num, "x", i, "=", num * i)
