# You can import by doing this
import os

# Prints current working directory
print(os.getcwd())

# We can change the current working directory
os.chdir("/home")
print(os.getcwd())

# List files and folders
print(os.listdir('/home'))

# You can scan a directory and get more info about it
with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, entry.is_file(), entry.is_dir())

# we can use os.mkdir()
os.mkdir("test")

# You can use this to create multiple directories
os.makedirs("directory")

# We can also use a method to remove directories as well
os.rmdir("directory-name")

# We use a method to rename a file or directory
os.rename('old.txt', 'new.txt')
