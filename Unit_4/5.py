# Program 35: Write a program to implement single, multilevel and multiple inheritance.
class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(B):
    def show_c(self):
        print("Class C")

class D:
    def show_d(self):
        print("Class D")

class E(A, D):
    pass

C().show_a()
C().show_b()
C().show_c()
E().show_d()
