from pydantic import BaseModel

# To extract a body from a request, we need to create a pydantic model of the request body
class LoginRequest(BaseModel):
    username: str
    password: str