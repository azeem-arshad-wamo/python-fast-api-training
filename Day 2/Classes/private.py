# We can create private variables (sort of)
class MyClass:
    def __init__(self):
        self.__secret = "SECRET"

first = MyClass()

# This is called name mangling
print(first._MyClass__secret)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # call parent method
        print(f"{self.name} barks loudly!")