from fastapi import APIRouter
from app.api.v1.endpoints import health, scoring, churn, validation

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(scoring.router, tags=["Scoring"])
api_router.include_router(churn.router, tags=["Churn"])
api_router.include_router(validation.router, tags=["Cross Validation"])
