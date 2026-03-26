from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/howdy")
async def wow():
    return {"message": "Howdy people"}