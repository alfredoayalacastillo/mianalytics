import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from app.models.schemas import CrossValidationRequest, CrossValidationResponse

class CrossValidatorService:
    def run_cross_validation(self, req: CrossValidationRequest) -> CrossValidationResponse:
        """Ejecuta Validación Cruzada K-Fold con Scikit-learn sobre un dataset."""
        # Dataset sintético/simulado de entrenamiento hasta conectar tablas reales de Corteza
        np.random.seed(42)
        n_samples = 100
        X = np.random.randn(n_samples, 4)
        y = np.random.randint(0, 2, size=n_samples)

        model = RandomForestClassifier(n_estimators=20, random_state=42)
        skf = StratifiedKFold(n_splits=req.n_splits, shuffle=True, random_state=42)
        
        scores = cross_val_score(model, X, y, cv=skf, scoring='accuracy')

        return CrossValidationResponse(
            dataset_name=req.dataset_name,
            n_splits=req.n_splits,
            mean_accuracy=round(float(scores.mean()), 4),
            std_accuracy=round(float(scores.std()), 4),
            scores=[round(float(s), 4) for s in scores],
            status="success"
        )

cross_validator_service = CrossValidatorService()
