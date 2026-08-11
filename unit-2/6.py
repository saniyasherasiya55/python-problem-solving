# Write a program to iterate over lists strings and dictionaries using loops. 

# ---------------- LIST ----------------

print("List Iteration")

# Creating a list
numbers = [10, 20, 30, 40, 50]

# Iterating through the list
for item in numbers:
    print(item)

# ---------------- STRING ----------------

print("\nString Iteration")

# Creating a string
name = "Python"

# Iterating through each character
for ch in name:
    print(ch)

# ---------------- DICTIONARY ----------------

print("\nDictionary Iteration")

# Creating a dictionary
student = {
    "Name": "Rahul",
    "Age": 20,
    "City": "Rajkot"
}

# Iterating through dictionary
for key, value in student.items():
    print(key, ":", value)
