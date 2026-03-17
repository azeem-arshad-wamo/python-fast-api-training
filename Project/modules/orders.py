import json

try:
    with open("Data/orders.json", "r") as f:
        orders = json.load(f)
except Exception as e:
    print(f"Error: {e}")
    orders = []


def createOrder(info):
    if not info or not info:
        raise Exception("Incorrect Information Provided")

    new_order = {
        "id": len(orders) + 1,
        "item": info,
        "status": "incomplete"
    }

    for order in orders:
        if order["item"] == new_order["item"]:
            raise Exception("Item Already Exists")

    orders.append(new_order)

    with open("Data/orders.json", "w") as f:
        json.dump(orders, f, indent=4)
    
    print("Order Created")


def viewOrders():
    if len(orders) > 0:
        print("_______________________________")
        for order in orders:
            print("---------------------")
            print(f"Order Id: {order["id"]}")
            print(f"Item: {order["item"]}")
            print(f"Status: {order["status"]}")
        print("_______________________________")
    else: 
        print("There are no orders")