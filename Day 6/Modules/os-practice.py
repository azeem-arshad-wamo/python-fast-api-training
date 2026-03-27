import os

os.system('clear')

# We can print files inside a folder
print(os.listdir("/home/mrmacbook/training/python-fastapi-training"))

# We can check if something is a file or folder
print(os.path.isdir("/home/mrmacbook/training/python-fastapi-training/"))
print(os.path.isfile("/home/mrmacbook/training/python-fastapi-training/"))

# We can join paths with os.
# Windows and Linux use different paths. It does it for you
print(os.path.join("../Modules", "args.py"))

# we can make folders with it too
os.makedirs("pdf", exist_ok=True)

# We can rename files with
os.rename("arg.py", "args-practice.py")