# 10.Write a program to demonstrate recursion using factorial or Fibonacci series. 

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("factorial of 5 is:",factorial(5))
