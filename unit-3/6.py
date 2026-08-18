# 6. Write a program to perform file and directory operations using os and sys modules. 

import os
import sys

print("current directory " , os.getcwd())

print("file and folder")
print(os.listdir())

print("python version " ,sys.version)
print("operating system ",os.name)

