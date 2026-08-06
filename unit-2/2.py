# 2. Write a program to check whether a number is positive negative or zero using nested conditions. 


num=int(input("enter the number:"))

if num >0:
     print(" number is positive")

if num % 2 == 0:
     print("number is even ")

else:
    print("number is odd ")

if num>0:
     print("number is positive")

elif num<0:
     print("number is negative")

else:
    print("zero")
