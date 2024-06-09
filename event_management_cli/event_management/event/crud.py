# event_management/event/crud.py

from sqlalchemy.orm import Session
from .models import Event

# Create an Event
def create_event(db: Session, name: str, date: str, location: str):
    db_event = Event(name=name, date=date, location=location)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

# Get all Events
def get_events(db: Session):
    return db.query(Event).all()

# Get an Event by ID
def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

# Update an Event
def update_event(db: Session, event_id: int, name: str = None, date: str = None, location: str = None):
    db_event = get_event(db, event_id)
    if db_event:
        if name:
            db_event.name = name
        if date:
            db_event.date = date
        if location:
            db_event.location = location
        db.commit()
        db.refresh(db_event)
    return db_event

# Delete an Event
def delete_event(db: Session, event_id: int):
    db_event = get_event(db, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event
