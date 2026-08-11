# . Write a program to demonstrate list dictionary and set comprehensions. 

# ---------------- LIST COMPREHENSION ----------------

# Create a list of square numbers
list1 = [x * x for x in range(1, 6)]

print("List Comprehension:")
print(list1)

# ---------------- DICTIONARY COMPREHENSION ----------------

# Create a dictionary with number and its square
dict1 = {x: x * x for x in range(1, 6)}

print("\nDictionary Comprehension:")
print(dict1)

# ---------------- SET COMPREHENSION ----------------

# Create a set of square numbers
set1 = {x * x for x in range(1, 6)}

print("\nSet Comprehension:")
print(set1)
