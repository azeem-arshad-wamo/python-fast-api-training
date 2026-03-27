from fastapi import APIRouter, Query
from typing import Annotated
from models.user_models import userUpdateRequest, updatePasswordRequest

router = APIRouter(prefix="/users")

# We can both make a query parameter optional as well as enforce a rule when it is provided
@router.get("/posts")
async def getPost(id: int, q: Annotated[str | None, Query(max_length=50)] = None):
    result = {}
    if q:
        result["q"] = q

    result["id"] = id
    return {
        "message": "Got the Posts",
        "result": result,
    }

# Older versions of fastApi used to define query parameters like this
# We can also add multiple validations
@router.get("/newPosts")
async def getPost(id: int, q: str | None = Query(default=None, min_length=5, pattern="^fixedquery$", max_length=50)):
    result = {}
    if q:
        result["q"] = q

    result["id"] = id
    return {
        "message": "Got the Posts",
        "result": result,
    }


# We can use @app.put to create a put method just like post one
@router.put("/{userId}")
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
@router.patch("/{userId}")
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
@router.delete("/{userId}")
async def deleteUser(userId: int):
    return {
        "message": f"User with ID: {userId} is deleted successfully"
    }

# We can simply add path parameters to a route the same way we can add a variable to a string in python
@router.get("/{id}")
async def getUserById(id: int):
    print(f"User Requested. ID: {id}")
    return { "message": "Done", "user": f"ID: {id}" }

# We can have both path and query parameters in one route
@router.get("/{user_id}/items/{item_id}")
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

