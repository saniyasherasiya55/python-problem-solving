# Program 34: Write a program to demonstrate instance methods, class methods and static methods.
class Demo:
    def instance_method(self):
        print("Instance method")
    @classmethod
    def class_method(cls):
        print("Class method")
    @staticmethod
    def static_method():
        print("Static method")

d = Demo()
d.instance_method()
Demo.class_method()
Demo.static_method()
