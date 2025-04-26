from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.event_schema import EventCreate, EventResponse
from app.models.event_model import Event
from app.core.config import SessionLocal
from app.services.ml_service import predict_attack as ml_predict

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EventResponse)
def predict_attack(event: EventCreate, db: Session = Depends(get_db)):
    # Use Machine Learning model to predict attack_type and risk_score
    prediction = ml_predict(event.source_ip, event.destination_ip)

    db_event = Event(
        source_ip=event.source_ip,
        destination_ip=event.destination_ip,
        attack_type=prediction["attack_type"],
        risk_score=prediction["risk_score"]
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
