# 7. Write a program to copy move and delete files using shut il module.

import shutil

shutil.copy("file.txt" , "copy.txt")
print("file copied")

shutil.move("copy.txt " , "newfolder/copy.txt")
print("file moved")

import os
os.remove("newfolder/copy.txt")
print("file deleted")
