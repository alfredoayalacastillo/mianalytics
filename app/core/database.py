import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import text
from app.core.config import settings

logger = logging.getLogger(__name__)

# Engine asíncrono para PostgreSQL / pgvector
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.ENVIRONMENT == "development",
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=5
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def check_db_health() -> dict:
    """Verifica conectividad con PostgreSQL y la disponibilidad de pgvector."""
    try:
        async with AsyncSessionLocal() as session:
            result = await session.execute(text("SELECT 1;"))
            row = result.scalar()
            
            # Verificar extensión pgvector
            vector_check = await session.execute(
                text("SELECT extname FROM pg_extension WHERE extname = 'vector';")
            )
            has_vector = vector_check.scalar() is not None

            return {
                "status": "connected" if row == 1 else "degraded",
                "pgvector_enabled": has_vector
            }
    except Exception as e:
        logger.warning(f"No se pudo conectar a PostgreSQL: {str(e)}")
        return {
            "status": "disconnected",
            "error": str(e),
            "pgvector_enabled": False
        }
