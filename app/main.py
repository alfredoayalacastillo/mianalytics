from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Cerebro Analítico Python para AI-Performia (Scikit-learn, Churn, Lead Scoring, Cross-Validation)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas API v1
app.include_router(api_router, prefix="/api/v1")

@app.get("/", include_in_schema=False)
async def root():
    return {
        "message": f"Bienvenido a {settings.PROJECT_NAME} API Engine",
        "docs": "/docs",
        "health": "/api/v1/health"
    }
