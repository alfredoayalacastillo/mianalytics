from fastapi import APIRouter
from app.core.config import settings
from app.core.database import check_db_health

router = APIRouter()

@router.get("/health", summary="Health check del microservicio MIANALITICS")
async def health_check():
    db_status = await check_db_health()
    return {
        "service": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT,
        "status": "online",
        "database": db_status
    }
