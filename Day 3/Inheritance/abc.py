# abc modules helps you avoid writing incomplete classes
from abc import ABC, abstractmethod

# We can use ABC module to enforce rules
# Here, any child class must also have a speak method of their own
# The abc module lets you create classes that cannot be used unless certain methods are implemented
class Animal(ABC):
    @abstractmethod
    def speak(self):
        print("Hi!")

class Dog(Animal):
    @property
    def speak(self):
        print("Bark")

d = Dog()
print(d.speak)