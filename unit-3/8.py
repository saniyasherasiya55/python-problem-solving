# 8. Write a program to demonstrate basic regular expression pattern matching. 

import re

text="number is 1234567895"

pattern =r"/d+"

result =re.search(pattern ,text)

if result:
    print("number fond :" , result.group())

else:
    print("number not found")
