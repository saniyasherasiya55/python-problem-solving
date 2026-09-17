# 10.Write a program to extract specific information from a text file using regular expressions.

import re

text ="""
            name:saniya sherasiya
            age:20 email:
            abc@gmail.com
                                        """
name=re.search(r"name:\s*(.*)", text ).group(1)
age=re.search(r"age:\s*(\d+)", text ).group(1)
email=re.search(r"email:\s*(\+)", text ).group(1)

print("name:" ,name)
print("age:" ,age)
print("email:" ,email)
