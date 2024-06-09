# event_management/event/models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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

class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    description = Column(String)
    event = relationship('Event', back_populates='schedules')

class Attendee(Base):
    __tablename__ = 'attendees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship('Event', back_populates='attendees')
