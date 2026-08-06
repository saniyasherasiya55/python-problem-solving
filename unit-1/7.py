# 7. Write a program to create a dictionary and demonstrate dictionary methods and iteration. 

a={'name':'saniya','age':20,'city':'wankaner'}
print("dictionary",a)
a.update({'age': 21})
a["course"]="python"
for key, value in a.items():
    print(key ,':' ,value)
