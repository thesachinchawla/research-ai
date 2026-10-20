from fastapi import APIRouter

router = APIRouter(prefix="/research", tags=["Research"])


@router.get("/")
async def get_research():
    return {"message": "Research endpoint is working"}