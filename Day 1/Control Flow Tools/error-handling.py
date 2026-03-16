# We can handle errors in python by using try-except blocks
# The following will throw an error. We can customize the error.
try:
    x = 10 / 0
except: 
    print("Cannot divide by 0 mate")

# You can specify different error messages for different kinds of errors
try:
    result = 10 / 0
except ValueError:
    print("You must enter a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# You can catch errors and print them out manually
try:
    x = 10 / 0
except Exception as e:
    print(f"Error: {e}")

# You can add an else block that executes when there is no error to be found
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print("Success! Result is", result)

# You can also add a finally block that exectues no matter if there was an error or not
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print("Success! Result is", result)
finally:
    print("Finished Work!")