from fastapi import APIRouter
from models.auth_models import LoginRequest
from models.enums import Dessert, ModelName

router = APIRouter()

# We can then use it like this.
@router.post("/login")
async def handleLogin(body: LoginRequest):
    print(f"Username: {body.username}")
    print(f"Password: {body.password}")
    print(body.model_dump())
    return {"message": "Let's figure out how to use fastapi"}

# You can also restraint path parameters by making an class that inherts ENUM
@router.get("/dessert/{desertName}")
async def getDeserts(desertName: Dessert):
    return {"message": f"{desertName.value} is being sent"}

# This is an example from the docs
@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# We can also have a path parameter contain and actual path
@router.get("/files/{filePath:path}")
async def getFile(filePath: str):
    return {"message": f"File Path: {filePath}"}

# We can add query parameters by simply adding new paramters to our function
@router.get("/user/")
async def getUserInfo(id: int, age: int):
    return {"message": "Success", "user": {"id": id, "age": age}}

@router.get("/info/")
async def sendInfo(id: int, user: str | None = None):
    if user:
        return {"message": "Done", "user": {"id": id, "user": user}}
    else:
        return {"message": "Half Done", "user": {"id": id, }}
    
