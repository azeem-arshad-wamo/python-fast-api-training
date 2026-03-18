# We can write a function by using the def syntax
def main():
    print("Main function executed")

main()

# We can add docstrings to a function. They are used to document functions.
def greet(name):
    """This functions greets the user"""
    print(f"Welcome {name}!")

greet("Goose")

# Functions return None by default if we don't return anything manually
print(greet("Goose")) # Prints None

# We can write default arguments in function parameters.
# This allows us to call a function with less arguments.

def SendEmail(user, retries = 4, recipient = "Asim"):
    while retries >= 0:
        if recipient in ["Asim", "Asif", "Raja"]:
            break
        print(f"Sending email from {user} to {recipient}")
        retries -= 1

# This is called positional arguments
SendEmail("Goose", 5, "Javed")

# You can also specify parameter names
# It is also called keyword arguments
SendEmail(user="John", retries=3, recipient="Snow")

# You can make a function parameters dynamic. Meaning, it can take any amount of parameters
# If there are multiple parameters, args must come after normal parameters
# Parameters after args become keyword only
def count(*args):
    print(f"Count: {sum(args)}")

count(3, 5, 6, 2, 1)

# You can also make a function recieve dynamic inputs and turn it into a dictionary
def output(**args):
    print(args)

output(name="Azeem", age=23)

# We can limit behaviour of arguments by allowing arguements to be passed in a certain way.
# / forces positional only 
# * forces keyword only
def welcome(name, age, /, joiningDate, *, applyDate,  probation):
    print(f"Welcome {name}")
    print(f"User Age: {age}")
    print(f"Joining Date: {joiningDate}")
    print(f"Applying Date: {applyDate}")
    print(f"Probabtion: {probation}")

welcome("Goose", 23, "Yesterday", applyDate="3 weeks ago", probation="in 3 months")

# We can create lambda functions too. 
# Lambda functions are functions without a name.
# Lambda function takes an argument and returns the result of an expression
square = lambda x : x **2
print(square(5))

# A lambda function can have multiple arguments
area = lambda x, y: x * y
print(area(5, 4))

# We often use a function that returns a lambda
def makeIncrementor(n):
    return lambda x: x + n

incr = makeIncrementor(5)
print(incr(5))
print(incr(5442))