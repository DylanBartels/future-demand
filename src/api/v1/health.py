from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def ping():
    """Health Check"""
    return {"ping": "pong!"}
