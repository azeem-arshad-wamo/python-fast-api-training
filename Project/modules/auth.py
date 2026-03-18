import os
import json
from modules.interface import handleInterface

def handleInput():
    os.system("clear")
    print("Welcome!\nLogin to start")
    email = input("Please enter your email:\n")
    password = input("Please enter your password:\n")

    try:
        result = login(email, password)
        print("Login Successful")
        print(result)
        handleInterface(result)
    except Exception as e:
        print(f"Something went wrong: {e}")


def login(email, password):
    if not email or not password: 
        raise Exception("Missing Credentials")
    
    with open("Data/users.json", "r") as f:
        users = json.load(f)

    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Done!")
            return user
         
    raise Exception("Invalid Credentials")