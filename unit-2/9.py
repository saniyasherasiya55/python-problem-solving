# Practical No.9.Write a program to demonstrate iterators and iterables in Python.


# Creating an iterable (List)
numbers = [10, 20, 30, 40]

print("Iterable:")
print(numbers)

# Converting iterable into iterator
it = iter(numbers)

print("\nIterator Output:")

# Accessing elements one by one
print(next(it))
print(next(it))
print(next(it))
print(next(it))
