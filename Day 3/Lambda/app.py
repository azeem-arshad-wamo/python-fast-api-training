# A lambda function takens an argument, returns the result of an expression
# A lamdba function can also be called an anonymous function
# We can write a lambda function this way

sum = lambda x, y: x + y
print(sum(3, 5))

# Another Example
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

# The following format is called an Immediately Invoked Function Expression (IIFE)
print((lambda x, y: x + y)(2, 3))

# A lambda function can be a higher-order function by taking a function (normal or lambda) as an argument like in the following contrived example:
high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))

print(high_ord_func(2, lambda x: x + 3))

# Lamdba functions are used with other methods too

# With map
numbers = [1, 2, 3, 4]

# Using a lambda
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16]

# Using a normal function
def square(x):
    return x ** 2
print(list(map(square, numbers)))  # [1, 4, 9, 16]


# Get even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [0, 2, 4, 6, 8]

# Using normal function
def is_even(x):
    return x % 2 == 0
print(list(filter(is_even, numbers)))  # [0, 2, 4, 6, 8]
