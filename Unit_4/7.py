# Program 37: Write a program to illustrate method resolution order and magic methods.
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

obj = B()
obj.show()
print(B.__mro__[0].__name__)
print(str(10))
