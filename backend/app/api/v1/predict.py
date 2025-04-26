from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.event_schema import EventCreate, EventResponse
from app.models.event_model import Event
from app.core.config import SessionLocal

router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EventResponse)
def predict_attack(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(
        source_ip=event.source_ip,
        destination_ip=event.destination_ip,
        attack_type=event.attack_type,
        risk_score=event.risk_score
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
