from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class LeadScoreRequest(BaseModel):
    tenant_id: str = Field(..., description="ID obligatorio del Tenant/Namespace para aislamiento estricto multi-tenant")
    deal_id: Optional[str] = Field(None, description="ID del Deal en Corteza CRM")
    deal_value: float = Field(..., description="Valor monetario estimado del Deal")
    interactions_count: int = Field(..., description="Número total de interacciones registradas")
    days_in_pipeline: int = Field(..., description="Días transcurridos en el pipeline comercial")
    stage_id: Optional[str] = Field(None, description="ID de la etapa actual")

class LeadScoreResponse(BaseModel):
    tenant_id: str = Field(..., description="ID del Tenant evaluado")
    deal_id: Optional[str] = None
    close_probability: float = Field(..., description="Probabilidad de cierre de 0.0 a 1.0")
    score_category: str = Field(..., description="Categoría: High, Medium, Low")
    key_factors: List[str] = Field(default_factory=list, description="Factores clave detectados")

class ChurnPredictionRequest(BaseModel):
    tenant_id: str = Field(..., description="ID obligatorio del Tenant/Namespace para aislamiento estricto multi-tenant")
    contact_id: Optional[str] = None
    account_id: Optional[str] = None
    inactivity_days: int = Field(..., description="Días sin interacción registrada")
    open_tickets_count: int = Field(0, description="Número de tickets abiertos")
    failed_campaigns_count: int = Field(0, description="Campañas sin respuesta")

class ChurnPredictionResponse(BaseModel):
    tenant_id: str = Field(..., description="ID del Tenant evaluado")
    contact_id: Optional[str] = None
    churn_risk_score: float = Field(..., description="Riesgo de churn de 0.0 a 1.0")
    risk_level: str = Field(..., description="Nivel: Critical, Warning, Safe")
    recommended_action: str = Field(..., description="Acción sugerida para mitigar churn")

class CrossValidationRequest(BaseModel):
    tenant_id: str = Field(..., description="ID obligatorio del Tenant/Namespace para aislamiento estricto multi-tenant")
    dataset_name: str = Field("deals", description="Nombre del dataset a validar ('deals', 'contacts')")
    n_splits: int = Field(5, description="Número de pliegues (K-Folds)")

class CrossValidationResponse(BaseModel):
    tenant_id: str = Field(..., description="ID del Tenant evaluado")
    dataset_name: str
    n_splits: int
    mean_accuracy: float
    std_accuracy: float
    scores: List[float]
    status: str
