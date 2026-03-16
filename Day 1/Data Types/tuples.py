# We can create tuples the same we do with arrays but using () rather than []
countries = ("Pakistan", "China", "United States", "United Kingdom")

print(type(countries))
# The primary difference between a list and a tuple is that, 
# a list can be changed and modified once created and a tuple cannot. 
print(countries)

# Since tuples are indexed, they can have duplicate values
countries = ("Pakistan", "China", "Pakistan")

# Note: You can change an item inside a tuple by converting it to a list, making the change and then converting it back to a tuple.
