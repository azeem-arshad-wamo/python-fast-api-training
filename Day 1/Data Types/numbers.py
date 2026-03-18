# Python automatically assigns types to variables
x = 4       # This is an integer variable
y = 2.4     # This is a flaot variable
z = 1j      # This is a complex variable

# We can verify variable types by using the type() method

print(type(x))
print(type(y))
print(type(z))

# We can convert from one type to another using int(), float() and complex() methods
print(float(x))
print(int(y))
print(complex(x));

# In python, we need to import a library to use random numbers
import random

print(random.randrange(2, 10))