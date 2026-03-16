# In python, booleans represent the value True and False
# The following variable would have a data type of bool
is_active = False

# We can check that by
print(type(is_active))

# Apart from explicitly assigning True or False,
# all values can be resolved to either True or False

# The following items will return True
print(bool("abc"))
print(bool(123)) 
print(bool(["apple", "cherry", "banana"]))

# The following items will return False
print(bool(None))
print(bool(0))
print(bool(""))