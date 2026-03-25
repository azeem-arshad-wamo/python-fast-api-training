# Python supports 5 main types of inheritances 

# 1. Single Inheritance. One Parent, One Child
class A:
    def show(self):
        print("A")

class B(A):
    pass

print(f"Single: {B.mro()}")

# Multiple Inheritances. One child, Multiple Parents
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()

print(f"Multiple: {C.mro()}")

# Multi Level Inheritence. Chained Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

print(f"Chained: {C.mro()}")

# Hierarchical Inheritance. One Parent, Multiple Child
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

print(f"Hierarchical: {C.mro()}")