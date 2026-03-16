# In python, set data type is not immutable and it cannot contain duplicate items.
# If we have a list like
items = ["Banana", "Orange", "Orange", "Peach", "Banana"]

# A set removes duplicates from that list
print(set(items))

# In a set, true and 1 is considered the same and therefore, the second occurence is removed.
info = {"apple", "banana", "cherry", True, 1, 2}
print(info)

# Similarly, false and 0 is handled the same
info = {"apple", "banana", "cherry", False, 0, 2}
print(info)

# Sets are not indexed but we can use a for in loop here.
for item in info:
    print(item)

