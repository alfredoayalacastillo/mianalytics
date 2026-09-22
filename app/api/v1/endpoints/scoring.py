from fastapi import APIRouter, HTTPException
from app.models.schemas import LeadScoreRequest, LeadScoreResponse
from app.services.ml_engine import ml_service

router = APIRouter()

@router.post("/predict/lead-score", response_model=LeadScoreResponse, summary="Predicción de Lead Scoring con Scikit-learn")
async def predict_lead_score(payload: LeadScoreRequest):
    try:
        return ml_service.predict_lead_score(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en inferencia de Lead Scoring: {str(e)}")
