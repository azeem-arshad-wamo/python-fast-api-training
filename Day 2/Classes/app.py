# To create a class, we use the class keyword
class Car:
    x = 5

    def __init__(self, name):
        # This method runs when we create a new object
        self.name = name
        print(f"New Car Created: {name}")
    
    def getName(self):
        return self.name

# We can now create an object by simply calling the class
myCar = Car("Toyota")

# We can access object attributes like this
print(f"Object Attribute: {myCar.x}")

print(f"Class Attribute: {Car.x}")

# We can use a getter method like this
print(myCar.getName())

# We can create a new attibute of an object like this
myCar.model = "Tacoma"

print(myCar.model)