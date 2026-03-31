from fastapi import APIRouter, Body
from pydantic import BaseModel, Field
from typing import Annotated

router = APIRouter(prefix="/body")

# We can set a body to be optional too
class Login(BaseModel):
    username: str
    email: str
    password: str

@router.post('/login')
async def login(body: Login | None = None):
    if not body:
        return {"message": "Cannot login without a body my friend"}
    else:
        return {"message": "Successfully logged in", "body": body}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# This will put the request body into a field called item.
@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

# We can add additional validation on request bodies as well
class Post(BaseModel):
    id: int
    title: str
    description: str = Field(
        default=None,
        title="The description of the item",
        description="Detailed description of the post that any user can make. This should include all the details one has to say",
        max_length=10000
    )

@router.post("/posts")
async def createPost(body: Post):
    return {"body": body}


# We can create a model inside a model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results