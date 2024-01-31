from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health",
    summary="/",
    description="ヘルスチェックAPI",
)
async def health_check():
    return "status is OK"
