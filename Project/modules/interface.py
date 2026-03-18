import os
from modules.orders import createOrder, viewOrders

def handleInterface(info):
    os.system("clear")

    if info["role"] == "admin":
        handleAdmin(info)
    elif info["role"] == "user":
        handleUser(info)
    else:
        raise Exception("Something went wrong")


def handleAdmin(info):
    while True:
        print(f"Welcome {info['username']}, you are an admin")
        print("______________________________________________")
        print("Press 1 to view user info")
        print("Press 2 to see orders")
        print("Press 0 to logout")

        option = input("Enter Option: ")
        os.system("clear")

        match option:
            case "0":
               return;
            case "1":
                print(info)
            case "2":
                print(viewOrders())
            case _:
                print("Invalid Option")

def handleUser(info):
    while True:
        print(f"Welcome {info['username']}, you are a customer")
        print("______________________________________________")
        print("Press 1 to view user info")
        print("Press 2 to place an order")
        print("Press 3 to check orders")
        print("Press 0 to logout")

        option = input("Enter Option: ")
        os.system("clear")

        match option:
            case "0":
                return
            case "1":
                print(info)
            case "2":
                print("________________________________")
                print("Enter Order Details:")
                order = input("Details: ")
                createOrder(order)
            case "3":
                viewOrders()