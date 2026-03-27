from pydantic import BaseModel

# We can use @app.put to create a put method just like post one
class userUpdateRequest(BaseModel):
    username: str
    email: str

# Patch follows the same pattern, just that we use it to update partial data
class updatePasswordRequest(BaseModel):
    password: str
    email: str | None = None