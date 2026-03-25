import os
os.system('clear')

# Let's make an empty class
class EmptyClass:
    pass

c = EmptyClass()
cMethod = dir(c)

print("Emtpy Class Object")
print(dir(c))

print()

o = object()
oMethod = dir(o)

print("Object method object")
print(dir(o))

difference = []

# This calculates the methods in dir(c) that are not available in dir(o)
for item in cMethod:
    if item not in oMethod:
        difference.append(item)


print()

print("Difference")
print(difference)