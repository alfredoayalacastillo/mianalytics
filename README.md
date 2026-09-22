# MIANALITICS - Cerebro Analítico Python (Microservicio AI-Performia)

Microservicio en Python (FastAPI + Scikit-learn + pgvector) dedicado al cálculo de modelos predictivos, scoring comercial, predicción de churn y validación cruzada para el ecosistema **AI-Performia**.

---

## 🚀 Características Principal

- **FastAPI + Uvicorn:** Endpoints REST asíncronos de ultra baja latencia.
- **Scikit-learn Engine:** Algoritmos de clasificación, regresión y validación cruzada K-Fold.
- **Conexión Directa PostgreSQL / pgvector:** Solo lectura optimizada para entrenamiento y búsquedas vectoriales.
- **Docker Ready:** Multistage build optimizado para desplegar en **Easypanel**.

---

## 🛠️ Instalación y Uso Local

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor en modo desarrollo
uvicorn app.main:app --reload --port 8000
```

Documentación interactiva disponible en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Pruebas Automatizadas

```bash
pytest
```

---

## 🐳 Despliegue en Easypanel

1. Crear servicio **App** usando la URL de este repositorio en GitHub.
2. Seleccionar **Dockerfile** como Build Method.
3. Exponer el puerto `8000`.
