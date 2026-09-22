from fastapi import APIRouter, HTTPException
from app.models.schemas import CrossValidationRequest, CrossValidationResponse
from app.services.cross_validator import cross_validator_service

router = APIRouter()

@router.post("/train/cross-validate", response_model=CrossValidationResponse, summary="Ejecutar Validación Cruzada Scikit-learn")
async def run_cross_validation(payload: CrossValidationRequest):
    try:
        return cross_validator_service.run_cross_validation(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en validación cruzada: {str(e)}")
