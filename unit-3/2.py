# 2.Write a program to demonstrate different import mechanisms in Python. 

import math
print("using import module")
print(math.sqrt(25))

from math import pow
print(pow(7,5))

from math import a
print(a.factorial(7))

from math import *
print(tan(0))
