from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventCreate(BaseModel):
    source_ip: str
    destination_ip: str
    attack_type: str
    risk_score: float

class EventResponse(BaseModel):
    id: int
    source_ip: str
    destination_ip: str
    attack_type: str
    risk_score: float
    created_at: datetime

    class Config:
        orm_mode = True
