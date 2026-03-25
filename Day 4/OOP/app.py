# Composition is when we create an object inside another object
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
# This means, Car has a Engine

# Inheritance means a class extends another class
# Meaning, it builds upon a base class
class Animal:
    pass

class Dog(Animal):
    pass
# Here, we extended another class

