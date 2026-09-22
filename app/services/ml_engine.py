import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from app.models.schemas import (
    LeadScoreRequest, LeadScoreResponse,
    ChurnPredictionRequest, ChurnPredictionResponse
)

class MLEngineService:
    def __init__(self):
        # Inicialización de pipeline básico pre-entrenado/demostración de Scikit-learn
        self.scaler = StandardScaler()
        self.scoring_model = LogisticRegression()

        # Fit sintético inicial para permitir inferencia in-memory
        X_dummy = np.array([
            [1000, 2, 60],
            [50000, 15, 10],
            [20000, 8, 30],
            [100000, 25, 5],
            [500, 1, 90]
        ])
        y_dummy = np.array([0, 1, 1, 1, 0])
        X_scaled = self.scaler.fit_transform(X_dummy)
        self.scoring_model.fit(X_scaled, y_dummy)

    def predict_lead_score(self, req: LeadScoreRequest) -> LeadScoreResponse:
        """Calcula la probabilidad de cierre usando Scikit-learn LogisticRegression."""
        features = np.array([[req.deal_value, req.interactions_count, req.days_in_pipeline]])
        features_scaled = self.scaler.transform(features)
        
        prob = float(self.scoring_model.predict_proba(features_scaled)[0][1])

        if prob >= 0.70:
            category = "High"
        elif prob >= 0.40:
            category = "Medium"
        else:
            category = "Low"

        factors = []
        if req.interactions_count >= 10:
            factors.append("Alta frecuencia de interacción comerciante")
        if req.days_in_pipeline <= 15:
            factors.append("Avance rápido en el pipeline")
        if req.deal_value >= 30000:
            factors.append("Deal de alto valor monetario")

        return LeadScoreResponse(
            deal_id=req.deal_id,
            close_probability=round(prob, 4),
            score_category=category,
            key_factors=factors or ["Métricas comerciales estándar"]
        )

    def predict_churn_risk(self, req: ChurnPredictionRequest) -> ChurnPredictionResponse:
        """Calcula el riesgo de churn para un contacto o cuenta."""
        # Heurística ponderada + regla estadística
        risk = min(1.0, (req.inactivity_days * 0.02) + (req.open_tickets_count * 0.15) + (req.failed_campaigns_count * 0.10))

        if risk >= 0.70:
            level = "Critical"
            action = "Asignar ejecutivo Senior para llamada inmediata de rescate"
        elif risk >= 0.40:
            level = "Warning"
            action = "Enviar campaña automatizada de re-engagement"
        else:
            level = "Safe"
            action = "Mantener comunicación periódica estándar"

        return ChurnPredictionResponse(
            contact_id=req.contact_id,
            churn_risk_score=round(risk, 4),
            risk_level=level,
            recommended_action=action
        )

ml_service = MLEngineService()
