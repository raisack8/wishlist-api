from fastapi import APIRouter

router = APIRouter()

@router.get(
        "/health",
        description="ヘルスチェック",
        )
async def health_check():
    return "status is OK"