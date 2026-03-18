# In python, we call arrays lists
# We can slice lists like strings
numbers = [2, 5, 8, 11, 82]

# We can concatinate two lists
Team_A = [1, 2, 3]
Team_B = [4, 5, 6]
Final = Team_A + Team_B

print(Final)

# Since lists are mutable, we can change them
Final[0] = 6
Final[-1] = 1

print(Final)

# You can add items to a list by using .append() method
Final.append(8)
print(Final)

# List items can have any data type
data = [4, "Apple", 5.3, ["a", "b"]]
print(data)

# We can create nested lists
New_Final = [Team_A, Team_B]
print(New_Final)