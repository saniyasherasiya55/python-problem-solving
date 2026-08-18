# 9.  Write a program to use re module functions such as match search and find all. 

import re

text= "python is easy. python is powerful"

print("match:" ,re.match("python",text))

print("search:" ,re.search("python",text))

print("find all:" ,re.findall("python",text))
