# There are 4 levels of scopes in python
# Local, Enclosing, Gloabl and Built-in, often remembered as LEGB

# This is a global variable
x = "global"

def outer():
    # This is a variable with enclosing scope
    x = "enclosing"

    def inner():
        # This is a variable with local scope
        x = "local"
        print(x)

    inner()

outer()

# In the example above, all three variables are seperate from each other. 
# We cannot modify a global variable inside a local scope.

# We can use global keyword to access the global variable
x = 10

def func():
    global x
    x = 20

func()
print(x)  # 20

# To access an enlcosing variable that is not global but is outside the current scope
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()  # 20