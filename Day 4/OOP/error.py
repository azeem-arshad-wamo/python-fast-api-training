# To raise an exception with a class, we need to extends the Exception class
class notAnError(Exception):
    pass

# We can now raise it

try:
    raise notAnError("Incorrect usage of class")
except Exception as e:
    print(f"Error; {e}")