# Program 36: Write a program to demonstrate method overriding and polymorphism.
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

Animal().sound()
Dog().sound()
