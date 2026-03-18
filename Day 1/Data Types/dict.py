# In python, we called an object a dictionary. With a difference that, the key is written in double quotes too.
data = {
    "name": "Goose",
    "age": 23,
    "city": "Lahore",
    "colors": ["orange", "black", "red"]
}
print(data)

# We can access all keys from a dictionary by using the dict.keys() methods
print(data.keys())

# We can also fetch just the values from a dictionary
print(data.values())

# The items() method will return each item in a dictionary, as tuples in a list.
print(data.items()) 

# We can also add a key value pair to a dictionary like this
data["country"] = "Pakistan"

print(data)

