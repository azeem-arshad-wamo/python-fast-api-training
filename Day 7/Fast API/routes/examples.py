from fastapi import APIRouter, Body
from typing import Annotated
from pydantic import BaseModel, Field

router = APIRouter(prefix="/examples")

# We can add an example to our model and it will show the example to the docs
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A notvery nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# When using field with Pydantic models, we can also add examples
class userInfo(BaseModel):
    username: str = Field(example="MyselfGoose")
    email: str = Field(example="azeem.arshad@wamolabs.com")
    password: str = Field(example="H2*4N!@4snN")

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "username": "MyselfGoose",
                    "email": "azeem.arshad@wamolabs.com",
                    "password": "goosegoose"
                }
            ]
        },
    }

@router.put("/useruser")
async def replaceUser(body: userInfo):
    return {"message": "user replaced", "body": body}

class userPatch(BaseModel):
    username: str
    email: str
    password: str

@router.patch("/user")
async def patchUser(
    body: Annotated[
        userPatch,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        )
    ]
):
    return {"body": body}