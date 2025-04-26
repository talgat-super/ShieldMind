from fastapi import FastAPI
from app.api.v1 import predict, alerts
from app.core.config import Base, engine
from app.models import event_model


app = FastAPI(
    title="ShieldMind API",
    version="1.0.0",
    description="Cyberattack prediction system using AI",
)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(predict.router, prefix="/api/v1/predict", tags=["Predict"])
app.include_router(alerts.router, prefix="/api/v1/alerts", tags=["Alerts"])

@app.get("/")
def root():
    return {"message": "Welcome to ShieldMind API"}
