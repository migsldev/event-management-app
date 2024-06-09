from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from event_management.database import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(DateTime)
    location = Column(String)
    schedules = relationship('Schedule', back_populates='event')
    attendees = relationship('Attendee', back_populates='event')
    users = relationship('User', secondary='user_event_association', back_populates='events')
