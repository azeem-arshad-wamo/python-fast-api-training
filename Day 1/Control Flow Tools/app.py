# We can use if statements to perforn actions based on some condition
age = 21

if age > 18:
    print("You are of legal age")
elif age == 18:
    print("You just got to the legal age")
else:
    print("You shouldn't be allowed to do anything")

# In python, we can use for loop to iterate over strings or arrays without explicing writing iterating logic
cars = ["Koenigsegg", "Buggatti", "Lamborghini", "Ferrari"]

for car in cars:
    print("Car Name: " + car);
    print("Car Length: ", len(car))

# It's also possible to iterate over a dictionary
users = {
    "Azeem": "active",
    "Omar": "in-active",
    "Ali": "active"
}

active_users = {}

for user, status in users.items():
    if(status == "active"):
        active_users[user] = status

print(active_users)


# We can use the break keyword to break out of a loop
data = [
    {
        "name": "Goose",
        "age": 23,
        "status": "active",
        "role": "user"
    },
    {
        "name": "Ali",
        "age": 25,
        "status": "in-active",
        "role": "admin"
    },
    {
        "name": "Wayne",
        "age": 56,
        "status": "active",
        "role": "user"
    },
    {
        "name": "Saad",
        "age": 24,
        "status": "in-active",
        "role": "user"
    },
]

# This loop immediately stops working as soon as the admin is found
for user in data: 
    if user["role"] == "admin":
        print(f"Admin Found. Name: {user["name"]}")
        break;

# We can also use continue keyword
for user in data:
    if user["status"] == "active":
        continue;

    print(f"Removing {user["name"]} from the database!")

# We can add an else clause to a for loop that executes after the last iteration of the loop, only when no breaks were made.
for user in data:
    if user["age"] < 18 or user["age"] > 60:
        print("Illegal person found")
        break;
else:
    print("Everything went good")    

# We also have a pass keyword that we use as placeholder to replace later.
# Here, we wrote the if statement but we added pass rather than logic. We can replace pass with logic later on.
if len(users) > 0:
    pass

# Python has something similar to a switch statement from JavaScript
option = 5
match option:
    case 0:
        print("Exiting...")
    case 1:
        print("Performing action 1")
    case 2:
        print("Performing action 2")
    case 3 | 4 | 5:
        print("Performing step 3, 4 and 5")
    case _:
        print("Could not perform any action")