from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from classes import router as classRouter

app = FastAPI()
app.include_router(classRouter)

# In fastAPI, any function can be a dependency when another function needs it to work
# The following function is a dependency that two routes are dependent on
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# We can further decrease code duplication by putting the result of Annotated into a variable
commonDep = Annotated[dict, Depends(common_parameters)]

@app.get("/items/")
async def read_items(commons: commonDep):
    return commons

@app.get("/users/")
async def read_users(commons: commonDep):
    return commons


# A use case for this would be the following routes.
def getCurrentUser(token: str):
    user = getUser(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unathorized")
    return user

def getUser(token: str):
    return "user info"

@app.get("/profile")
async def getProfile(user =  Depends(getCurrentUser)):
    return {"profile": "Profile data"}

@app.get("/orders")
async def get_orders(user = Depends(getCurrentUser)):
    return {"orders": [], "user": user}

# We can also do an admin restriction
def isAdmin(token: str):
    if token == "admin":
        return True
    else:
        raise HTTPException(status_code=404, detail="Unauthorized")
    
# We can manually tell a dependency to use cache as well
@app.delete("post")
async def deletePost(isAdmin = Depends(isAdmin, use_cache=True)):
    return {"status": "deleted"}


# Sometimes, we need a depdency to do the work but we don't need their result. For authorization or other checks.
# We can write a decorator dependency in our route that runs the dependencies but don't return their results
@app.get("/test", dependencies=[Depends(isAdmin)])
async def testFunction(token: str):
    return {"message": "You are an admin"}