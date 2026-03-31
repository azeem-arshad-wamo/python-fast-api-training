from fastapi import APIRouter, Query, Depends
from pydantic import AfterValidator, BaseModel, Field
from typing import Annotated

router = APIRouter(prefix="/query")

# As we learned previously, we can make a parameter optional and also enforce rules if a value is provided.
# We can use Annotated to do that
@router.get("/user")
async def getUser(id: int, q: Annotated[str | None, Query(min_length=4, max_lengt=40)] = None):
    return {
        "message": "One query parameter is optional. One is not",
        "id": f"Not Optional. ID: {id}",
        "q": f"q was provided. q: {q}" if q else f"q was not provided. "
    }

# We can achieve similar thing by using an older method
@router.get("/post")
async def getPost(id: int, q: str | None = Query(default=None, min_length=4, max_length=40)):
    return {
        "message": "One query parameter is optional. One is not",
        "id": f"Not Optional. ID: {id}",
        "q": f"q was provided. q: {q}" if q else f"q was not provided. "
    }

# We can force user to provide a value, even if the value is None.
# We can do that by removing the default value from a query parameter
@router.get("/user")
async def getUser(id: int, q: Annotated[str | None, Query(min_length=4, max_lengt=40)]):
    return {
        "message": "One query parameter is optional. One is not",
        "id": f"Not Optional. ID: {id}",
        "q": f"q was provided. q: {q}" if q else f"q was not provided. "
    }

# We can make a query parameter appear multiple times in an api route.
# It will add all appearances of a path parameter in a list
# We can add a default list value too
@router.get("/post")
async def getPost(id: int, q: Annotated[list[str] | None, Query()] = ["foo", "bar"]):
    return {
        "message": "One query parameter is optional. One is not",
        "id": f"Not Optional. ID: {id}",
        "q": f"q was provided. q: {q}" if q else f"q was not provided."
    }


# We can also add a title and a description that will appear in our API doc
@router.get("/comment")
async def getComments(
    id: int,
    username: Annotated[
        str | None,
        Query(
            title="Get comment from id",
            description="You can fetch a comment data by providing a comment id to the server. username is optional.",
            min_length=4
        )
    ] = None
):
    return {"id": id, "username": username}

# Sometimes, we need a parameter like item-query but that is not allowed in python.
# We can declare that as an alias and python will handle the rest
@router.get("/comment")
async def getNewComment(id: Annotated[str | None, Query(alias="comment-id")] = None):
    return {"message": "Alias done", "id": id}

# We can show that a parameter is depreciated in our docs as well
@router.get("/depreciation")
async def getComments(
    id: int,
    username: Annotated[
        str | None,
        Query(
            title="Depreciated Parameter",
            description="This parameter is marked depreciated and will be shown as depreciated inside our documentation",
            min_length=4,
            deprecated=True
        )
    ] = None
):
    return {"id": id, "username": username}

# Similarly, we can hide a parameter from the docs by adding another option
@router.get("/hide")
async def getComments(
    id: int,
    username: Annotated[
        str | None,
        Query(
            title="Hidden Parameter",
            description="This parameter would be hidden inside the docs",
            min_length=4,
            include_in_schema=False
        )
    ] = None
):
    return {"id": id, "username": username}

# Practice Data
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

# We can add a post validator function that runs validation after initial validations
def checkValidId(id: str):
    if not id:
        raise ValueError("ID not provided")
    
    if not id.startswith(("isbn", "imdb")):
        raise ValueError("Incorrect format of ID provided. It must start with imdb or isbn")

    return id

@router.get("/")
async def getBook(id: Annotated[str | None, AfterValidator(checkValidId)] = None):
    if not id:
        return {"message": "Please provide a valid id"}

    if id:
        item = data.get(id)

    if not item:
        return {"message": "Couldn't find any item with that id"}

    return {"message": "data found", "data": item}

# We can write a pydantic model to structure a query parameter
# It stores as a pydantic model object
# We can also restrict any extra query parameters
class Filter(BaseModel):
    model_config = {"extra": "forbid"}
    limit: int = Field(25, le=100, gt=5)
    offset: int = Field(2, gt=0)
    tags: list[str] = Field(default_factory=list)

@router.get("/filter")
async def filtered(filters: Annotated[Filter, Query()]):   
    return {"message": "Filters work", "filters": filters}