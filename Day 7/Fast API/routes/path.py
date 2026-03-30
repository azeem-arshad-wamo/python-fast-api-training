from fastapi import APIRouter, Path, Query
from typing import Annotated

router = APIRouter(prefix="/path")

# We can do the same kind of validation for path parameters as well
@router.get("/user/{id}")
async def getUser(
    id: Annotated[int, Path(title="The id of the user to fetch", lt=100)],
    age: Annotated[int, Query(ge=18, lt=100)],
    username: Annotated[
        str | None,
        Query(
            title="Optional username filed",
            description="Optional username field. Allows more precise searching and can bring faster results",
            min_length=4,
            max_length=30
        )
    ] = None,
    
):
    return {
        "message": "User Found",
        "id": id,
        "age": age if age else "Underage",
        "username": username if username else "Username not provided"
    }