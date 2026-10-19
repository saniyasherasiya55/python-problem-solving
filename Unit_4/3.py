# Program 33: Write a program to illustrate instance variables and class variables.
class Student:
    college = "Marwadi University"
    def __init__(self, name):
        self.name = name

s = Student("Saniya")
print("Name :", s.name)
print("College :", Student.college)
