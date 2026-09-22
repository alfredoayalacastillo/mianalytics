from fastapi import APIRouter, HTTPException
from app.models.schemas import ChurnPredictionRequest, ChurnPredictionResponse
from app.services.ml_engine import ml_service

router = APIRouter()

@router.post("/predict/churn", response_model=ChurnPredictionResponse, summary="Predicción de Riesgo de Churn")
async def predict_churn(payload: ChurnPredictionRequest):
    try:
        return ml_service.predict_churn_risk(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en inferencia de Churn: {str(e)}")
