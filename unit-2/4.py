# 4. Write a program to find the sum of digits of a number using a while loop. 

num = int(input("Enter a number: "))


sum = 0


while num > 0:

 
    digit = num % 10

    sum = sum + digit

   
    num = num // 10

<<<<<<< HEAD
print("Sum of digits =", sum)
=======
print("Sum of digits =", sum)
>>>>>>> 9e4e5e96d04ad1512ec4f64e04b081f0d35dd146
