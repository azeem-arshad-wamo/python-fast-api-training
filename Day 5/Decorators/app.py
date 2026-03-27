import asyncio
import time
import os

os.system("clear")

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

print(add(5, 3))

def requireLogin(func):
    def wrapper(user, *args, **kwargs):
        if not user["status"] == "logged in":
            raise Exception("Unauthorized")
        return func(user, *args, **kwargs)
    return wrapper

@requireLogin
def getProfile(user):
    return f"Welcome User {user}"

user = {
    "username": "goose",
    "status": "logged out"
}

try:
    print(getProfile(user))
except Exception as e:
    print(f"Error: {e}")

# Timer Decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start}")
        return result
    return wrapper

@timer
def getData(id):
    result = id
    time.sleep(2)
    print(f"Done! Result: {result}")

getData(4)

def asyncDecorator(func):
    async def wrapper(*args, **kwargs):
        print("Before async function")
        result = await func(*args, **kwargs)
        print("After asycn method")
        return result
    return wrapper

@asyncDecorator
async def fetchData(name):
    await asyncio.sleep(2)
    print(f"Data fetched for {name}")

asyncio.run(fetchData("Goose"))

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hi():
    print("hi")

hi()

def log(func):
    async def wrapper(*args, **kwargs):
        print("Calling function")
        result = await func(*args, **kwargs)
        print("Finished")
        return result
    return wrapper


@log
async def fetch():
    return "data"

asyncio.run(fetch())