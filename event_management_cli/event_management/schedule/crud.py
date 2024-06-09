# event_management/schedule/crud.py
from sqlalchemy.orm import Session
from .models import Schedule

# Add a Schedule
def add_schedule(db: Session, event_id: int, start_time: str, end_time: str, description: str):
    db_schedule = Schedule(event_id=event_id, start_time=start_time, end_time=end_time, description=description)
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

# Get all Schedules for an Event
def get_schedules_for_event(db: Session, event_id: int):
    return db.query(Schedule).filter(Schedule.event_id == event_id).all()

# Get a Schedule by ID
def get_schedule(db: Session, schedule_id: int):
    return db.query(Schedule).filter(Schedule.id == schedule_id).first()

# Update a Schedule
def update_schedule(db: Session, schedule_id: int, start_time: str = None, end_time: str = None, description: str = None):
    db_schedule = get_schedule(db, schedule_id)
    if db_schedule:
        if start_time:
            db_schedule.start_time = start_time
        if end_time:
            db_schedule.end_time = end_time
        if description:
            db_schedule.description = description
        db.commit()
        db.refresh(db_schedule)
    return db_schedule

# Remove a Schedule
def remove_schedule(db: Session, schedule_id: int):
    db_schedule = get_schedule(db, schedule_id)
    if db_schedule:
        db.delete(db_schedule)
        db.commit()
    return db_schedule
