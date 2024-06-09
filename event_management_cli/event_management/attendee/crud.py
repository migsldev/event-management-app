# event_management/attendee/crud.py

from sqlalchemy.orm import Session
from .models import Attendee

# Register an Attendee
def register_attendee(db: Session, name: str, email: str, event_id: int):
    db_attendee = Attendee(name=name, email=email, event_id=event_id)
    db.add(db_attendee)
    db.commit()
    db.refresh(db_attendee)
    return db_attendee

# Get all Attendees for an Event
def get_attendees_for_event(db: Session, event_id: int):
    return db.query(Attendee).filter(Attendee.event_id == event_id).all()

# Get an Attendee by ID
def get_attendee(db: Session, attendee_id: int):
    return db.query(Attendee).filter(Attendee.id == attendee_id).first()

# Update an Attendee
def update_attendee(db: Session, attendee_id: int, name: str = None, email: str = None):
    db_attendee = get_attendee(db, attendee_id)
    if db_attendee:
        if name:
            db_attendee.name = name
        if email:
            db_attendee.email = email
        db.commit()
        db.refresh(db_attendee)
    return db_attendee

# Remove an Attendee
def remove_attendee(db: Session, attendee_id: int):
    db_attendee = get_attendee(db, attendee_id)
    if db_attendee:
        db.delete(db_attendee)
        db.commit()
    return db_attendee
