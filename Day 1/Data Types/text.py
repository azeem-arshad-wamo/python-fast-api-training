# Printing Texts.
# Using single quotes ('') or double quotes ("") give the same result
print("Spam Eggs") 
print('No eggs for anyone')

# To print a quote, we can add "\" to escape it and print
print('doesn\'t')
# Alternativetly, we can use different type of quotes to achieve the same thing
print("doesn't")

print("\"Yes\", he said to me")

print("isn't it true?")

# We can add new line by adding \n
print("First Line\nSecond Line")

# We can add a tab with "\t"
print("Name: \tGoose")

# We can ignore escape sequence by adding a r before the string
print(r"\"Yes\", he said to me")

# We can print multiple lines by using """[text goes here]""" or '''[text goes here]'''
print("""
    This is a multi line printing thing:
      1. First point goes here
      2. Second point goes here
        - Sub Point in second point
""")

# We can achieve the same thing with single quotes
print('''
    This is a multi line printing thing:
      1. First point goes here
      2. Second point goes here
        - Sub Point in second point
''')

# We can repeat strings by using the "*" operator with the string
print(3 * "yeet ")

# We can concatinate strings with + operator
print(3 * "Well, " + "What do we have here!")

# Strins next to each other with automatically concatinate
print("We ""will ""concatinate")

# We can index strings in the traditional way
name = "Goose"
print(name[0])
print(name[3])

# We can index from the end by using negative numbers
print(name[-1])
print(name[-3])

# Strings also support slicing.
print(name[2:5]) # Start at index 2, stop at 5
print(name[2:-1]) # Start at index 2, stop at -1

# Slicing can have defaults
print(name[:3]) # This starts from 0, stops at 3
print(name[4:]) # Start at index 4, stop at the end
print(name[-2:]) # start at index -2, stop till the end

string = "alphabetagamma"
print(len(string))
