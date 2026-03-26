from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/howdy")
async def wow():
    return {"message": "Howdy people"}

# To extract a body from a request, we need to create a pydantic model of the request body
class LoginRequest(BaseModel):
    username: str
    password: str

# We can then use it like this.
@app.post("/login")
async def handleLogin(body: LoginRequest):
    print(f"Username: {body.username}")
    print(f"Password: {body.password}")
    return {"message": "Let's figure out how to use fastapi"}

# We can use @app.put to create a put method just like post one
class userUpdateRequest(BaseModel):
    username: str
    email: str

@app.put("/users/{userId}")
async def updateUserInfo(userId: int, body: userUpdateRequest):
    return {
        "message": "Put Request Complete",
        "user": {
            "id": userId,
            "email": body.email,
            "username": body.username
        }
    }

# Patch follows the same pattern, just that we use it to update partial data
class updatePasswordRequest(BaseModel):
    password: str
    email: str | None = None

@app.patch("/users/{userId}")
async def updatePassword(userId: int, body: updatePasswordRequest):
    result = {}
    if body.email:
        result["email"] = body.email
    result["password"] = body.password
    return {
        "message": "Patch request complete",
        "user": result
    }

# We can use a delete method for deleting resources. Doesn't need a body
@app.delete("/users/{userId}")
async def deleteUser(userId: int):
    return {
        "message": f"User with ID: {userId} is deleted successfully"
    }


# We can simply add path parameters to a route the same way we can add a variable to a string in python
@app.get("/users/{id}")
async def getUserById(id: int):
    print(f"User Requested. ID: {id}")
    return { "message": "Done", "user": f"ID: {id}" }

# You can also restraint path parameters by making an class that inherts ENUM
class Dessert(str, Enum):
    cake = "cake"
    icecream = "ice cream"
    pie = "pie"

@app.get("/dessert/{desertName}")
async def getDeserts(desertName: Dessert):
    return {"message": f"{desertName.value} is being sent"}

# This is an example from the docs
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # We can use model_name.value to extract specific information from the path
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# We can also have a path parameter contain and actual path
# To do that, we would need to add :path after the paramter
@app.get("/files/{filePath:path}")
async def getFile(filePath: str):
    return {"message": f"File Path: {filePath}"}

# We can add query parameters by simply adding new paramters to our function
@app.get("/user/")
async def getUserInfo(id: int, age: int):
    return {"message": "Success", "user": {"id": id, "age": age}}

@app.get("/info/")
async def sendInfo(id: int, user: str | None = None):
    if user:
        return {"message": "Done", "user": {"id": id, "user": user}}
    else:
        return {"message": "Half Done", "user": {"id": id, }}

# We can have both path and query parameters in one route
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
