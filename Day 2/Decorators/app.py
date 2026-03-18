# We can add a decorator to a function to add additional behaviour to it
def decorator(func):
    def wrapper():
        print("Before executing the function")
        func()
        print("After executing the function")
    return wrapper

@decorator
def main():
    print("doing main things")

main()

# We can make a decorator with arguments as well
def argumented(func):
    def wrapper(*args, **kwargs):
        print("Before argumented function")
        result = func(*args, **kwargs)
        print("After argumented function")
        return result
    return wrapper

@argumented
def second(name):
    print(f"Welcome {name}!")

second("Goose!")

# We have some built-in decorators 
class Math:
    @staticmethod
    def add(x, y):
        return x + y
    
# Now, we can access it directly
print(Math.add(5, 2))

