# 5.  Write a program to display current date and time using date time module. 

import datetime

now=datetime.datetime.now()

print("current date " , now.date())
print("current time" , now.time())
